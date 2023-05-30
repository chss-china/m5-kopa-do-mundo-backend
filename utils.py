from datetime import datetime


class InvalidYearCupError(Exception):
    def __init__(self, message="there was no world cup this year"):
        self.message = message
        super().__init__(self.message)


class ImpossibleTitlesError(Exception):
    def __init__(self, message="impossible to have more titles than disputed cups"):
        self.message = message
        super().__init__(self.message)


class NegativeTitlesError(Exception):
    def __init__(self, message="titles cannot be negative"):
        self.message = message
        super().__init__(self.message)


def data_processing(selection_info):
    first_cup_str = selection_info.get("first_cup")
    titles = int(selection_info.get("titles"))

    first_cup = datetime.strptime(first_cup_str, "%Y-%m-%d").date()

    if titles < 0:
        raise NegativeTitlesError()

    if first_cup.year < 1930 or (first_cup.year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    expected_titles = (datetime.now().year - first_cup.year) // 4
    if titles > expected_titles:
        raise ImpossibleTitlesError()
