import locale
import sys
from datetime import datetime

from src.langues.LangueAnglaise import LangueAnglaise
from src.langues.LangueFrancaise import LangueFrancaise
from src.Ohce import Ohce
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class SystemLangAdapter():
    def __init__(self):
        langue_systeme = locale.getdefaultlocale()[0]
        self.__langue = LangueAnglaise() \
            if langue_systeme == "en_GB" \
            else LangueFrancaise()


class SystemHourAdapter():
    def __init__(self):
        heure_systeme = datetime.now().hour

        if heure_systeme >= 6 and heure_systeme < 12:
            self.__periode_journee = PeriodeDeLaJournee.MATIN
        elif heure_systeme >= 12 and heure_systeme < 18:
            self.__periode_journee = PeriodeDeLaJournee.APRES_MIDI
        elif heure_systeme >= 18 and heure_systeme < 22:
            self.__periode_journee = PeriodeDeLaJournee.SOIR
        else:
            self.__periode_journee = PeriodeDeLaJournee.NUIT


if __name__ == '__main__':
    o = Ohce(SystemLangAdapter(), PeriodeDeLaJournee.NUIT)
