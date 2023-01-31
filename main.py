import locale
import sys
from datetime import datetime

from src.langues.LangueAnglaise import LangueAnglaise
from src.langues.LangueFrancaise import LangueFrancaise
from src.Ohce import Ohce
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class SystemAdapter:
    def __init__(self, langue, periode_journee):
        self.__langue_sys = langue
        self.__langue = LangueAnglaise() if self.__langue_sys == "en_GB" else LangueFrancaise()
        self.__periode_journee = periode_journee

    def systemLangAdapter(self):
        return self.__langue

    def systemHourAdapter(self):
        if "6" <= heure < "12":
            self.__periode_journee = PeriodeDeLaJournee.MATIN
        elif "12" <= heure < "18":
            self.__periode_journee = PeriodeDeLaJournee.APRES_MIDI
        elif "18" <= heure < "22":
            self.__periode_journee = PeriodeDeLaJournee.SOIR
        elif "22" <= heure < "6":
            self.__periode_journee = PeriodeDeLaJournee.NUIT
        return self.__periode_journee


if __name__ == '__main__':
    heure = datetime.now().strftime("%H")
    langue = locale.getlocale()[0]

    o = Ohce(SystemAdapter(langue, heure).systemLangAdapter(), SystemAdapter(langue, heure).systemHourAdapter())
    print(o.dire_bonjour())
    print("Entrez un mot :")
    mot = sys.stdin.readline()
    print(o.palindrome(mot))
    print(o.dire_au_revoir())
