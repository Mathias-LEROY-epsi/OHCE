from src.langues.Constantes import Constantes
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueFrancaise:

    def dire_bonjour(self, periode_journee):
        return Constantes.Francais.BONSOIR \
            if periode_journee in (PeriodeDeLaJournee.SOIR, PeriodeDeLaJournee.NUIT) \
            else Constantes.Francais.BONJOUR

    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT

    def au_revoir(self):
        return Constantes.Francais.AU_REVOIR
