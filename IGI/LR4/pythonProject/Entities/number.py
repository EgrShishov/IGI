class Number:

    def __init__(self, numeral: int, denominator: int):
        #print(f'Создан объект')
        if denominator < 0:
            denominator *= -1
        self.number = {'numeral': numeral, 'denominator': denominator}
        #print(self.number)

    def values(self):
        return self.number

    @property
    def numeral(self):
        return self.number.get('numeral')

    @property
    def denominator(self):
        return self.number.get('denominator')

    def __eq__(self, other):
        return self.numeral * other.denominator == other.numeral * self.denominator

    def __lt__(self, other):
        value = (self.numeral * other.denominator - other.numeral * self.denominator)
        return value < 0 and value / (self.denominator * other.denominator) < 0

    def __le__(self, other):
        value = (self.numeral * other.denominator - other.numeral * self.denominator)
        return value <= 0 and value / (self.denominator * other.denominator) <= 0

    def __ge__(self, other):
        value = (self.numeral * other.denominator - other.numeral * self.denominator)
        return value >= 0 and value / (self.denominator * other.denominator) >= 0

    def __gt__(self, other):
        value = (self.numeral * other.denominator - other.numeral * self.denominator)
        return value > 0 and value / (self.denominator * other.denominator) > 0

    def __str__(self):
        return f'{self.number.get("numeral")}/{self.number.get("denominator")}'
