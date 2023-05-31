from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
from rest_framework import status
from .serializers import TeamSerializer
from exceptions import InvalidYearCupError
from exceptions import NegativeTitlesError
from exceptions import ImpossibleTitlesError
from utils import data_processing
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist


class TeamAPIView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        team_for = [model_to_dict(team) for team in teams]
        return Response(team_for)


    def post(self, request):
        data = request.data
        
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            try:
                selection_info = serializer.validated_data
                first_cup = selection_info.get('first_cup')
                if first_cup:
                    selection_info['first_cup'] = first_cup.isoformat()
                data_processing(selection_info)
                team = serializer.save()
                response_data = {
                    "id": team.id,
                    "name": team.name,
                    "titles": team.titles,
                    "top_scorer": team.top_scorer,
                    "fifa_code": team.fifa_code,
                    "first_cup": team.first_cup
                }
                
                return Response(response_data, status=201)
            except InvalidYearCupError as e:
                return Response({"error": e.message}, status=400)
            except NegativeTitlesError as e:
                return Response({"error": e.message}, status=400)
            except ImpossibleTitlesError as e:
                return Response({"error": e.message}, status=400)
        return Response(serializer.errors, status=400)
    
class TeamDetailView(APIView):
    def get(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
            serializer = TeamSerializer(team, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
            team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)