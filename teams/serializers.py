from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    first_cup = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Team
        fields = '__all__'