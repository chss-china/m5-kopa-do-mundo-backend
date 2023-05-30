from utils import data_processing
from utils import ImpossibleTitlesError
from utils import InvalidYearCupError
from utils import NegativeTitlesError

selection_info = {"first_cup": "1932-10-18", "titles": "4"}

try:
    data_processing(selection_info)
    print("Processamento de dados concluído com sucesso!")
except InvalidYearCupError as e:
    print(e.message)
except NegativeTitlesError as e:
    print(e.message)
except ImpossibleTitlesError as e:
    print(e.message)
