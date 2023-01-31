from src.langues.Constantes import Constantes
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueAnglaise:

    def salutation(self, periode_journee):
        if periode_journee == PeriodeDeLaJournee.MATIN:
            return Constantes.Anglais.GOOD_MORNING
        elif periode_journee == PeriodeDeLaJournee.APRES_MIDI:
            return Constantes.Anglais.GOOD_AFTERNOON
        elif periode_journee == PeriodeDeLaJournee.SOIR:
            return Constantes.Anglais.GOOD_EVENING
        elif periode_journee == PeriodeDeLaJournee.NUIT:
            return Constantes.Anglais.GOOD_NIGHT
        else:
            return Constantes.Anglais.GOOD_MORNING

    def bien_dit(self):
        return Constantes.Anglais.WELL_DONE

    def dire_au_revoir(self, periode_journee):
        return Constantes.Anglais.GOODBYE
