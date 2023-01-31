from src.langues.Constantes import Constantes
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueFrancaise:

    def salutation(self, periode_journee):
        if periode_journee == PeriodeDeLaJournee.MATIN:
            return Constantes.Francais.BONJOUR
        elif periode_journee == PeriodeDeLaJournee.APRES_MIDI:
            return Constantes.Francais.BON_APRES_MIDI
        elif periode_journee == PeriodeDeLaJournee.SOIR:
            return Constantes.Francais.BONSOIR
        elif periode_journee == PeriodeDeLaJournee.NUIT:
            return Constantes.Francais.BONNE_NUIT
        else:
            return Constantes.Francais.BONJOUR

    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT

    def dire_au_revoir(self, periode_journee):
        return Constantes.Francais.AU_REVOIR
