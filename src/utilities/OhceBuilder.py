from src.Ohce import Ohce
from src.PeriodeDeLaJournee import PeriodeDeLaJournee
from src.utilities.LangueStub import LangueStub


class OhceBuilder:
    def __init__(self):
        self.__langue = LangueStub()
        self.__periode_journee = PeriodeDeLaJournee.MATIN

    def build(self):
        return Ohce(self.__langue, self.__periode_journee)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def ayant_pour_langue(self, langue):
        self.__langue = langue
        return self

    def ayant_pour_periode_de_la_journee(self, periode_journee):
        self.__periode_journee = periode_journee
        return self
