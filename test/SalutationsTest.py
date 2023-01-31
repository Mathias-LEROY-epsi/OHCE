import parameterized.parameterized
import unittest

from src.langues.Constantes import Constantes
from src.langues.LangueAnglaise import LangueAnglaise
from src.langues.LangueFrancaise import LangueFrancaise
from src.utilities.OhceBuilder import OhceBuilder
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class SalutationsTest(unittest.TestCase):
    @parameterized.parameterized.expand(
        [
            [LangueAnglaise(), PeriodeDeLaJournee.MATIN, Constantes.Anglais.GOOD_MORNING],
            [LangueAnglaise(), PeriodeDeLaJournee.APRES_MIDI, Constantes.Anglais.GOOD_AFTERNOON],
            [LangueAnglaise(), PeriodeDeLaJournee.SOIR, Constantes.Anglais.GOOD_EVENING],
            [LangueAnglaise(), PeriodeDeLaJournee.NUIT, Constantes.Anglais.GOOD_NIGHT],
            [LangueFrancaise(), PeriodeDeLaJournee.MATIN, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), PeriodeDeLaJournee.APRES_MIDI, Constantes.Francais.BON_APRES_MIDI],
            [LangueFrancaise(), PeriodeDeLaJournee.SOIR, Constantes.Francais.BONSOIR],
            [LangueFrancaise(), PeriodeDeLaJournee.NUIT, Constantes.Francais.BONNE_NUIT],
        ],
        lambda _, __, args:
        "test_bonjour : ETANT DONNE un utilisateur parlant la langue %s \n"
        "ET que la période de la journée est %s \n"
        "QUAND on saisit une chaîne \n"
        "ALORS la salutation %s est envoyée avant toute réponse"
        % (str(type(args.args[0]).__name__), str(type(args.args[1]).__name__), args.args[2])
    )
    def test_bonjour(self, langue, periode_journee, attendu):
        o = OhceBuilder() \
            .ayant_pour_langue(langue) \
            .ayant_pour_periode_de_la_journee(periode_journee) \
            .build()

        result = o.dire_bonjour() + '\n' + o.palindrome("test")
        self.assertEqual(attendu, result[0:len(attendu)])

    @parameterized.parameterized.expand(
        [
            [LangueFrancaise(), PeriodeDeLaJournee.MATIN, Constantes.Francais.AU_REVOIR],
        ],
        lambda _, __, args:
        "test_au_revoir : ETANT DONNE un utilisateur parlant la langue %s \n"
        "ET que la période de la journée est %s \n"
        "QUAND on saisit une chaîne \n"
        "ALORS la salutation %s est envoyée à la fin"
        % (str(type(args.args[0]).__name__), str(type(args.args[1]).__name__), args.args[2])
    )
    def test_au_revoir(self, langue, periode_journee, salutation):
        o = OhceBuilder() \
            .ayant_pour_langue(langue) \
            .ayant_pour_periode_de_la_journee(periode_journee) \
            .build()

        result = o.palindrome("test") + ', ' + o.dire_au_revoir()
        self.assertEqual(salutation, result[-len(salutation):])


if __name__ == '__main__':
    unittest.main()
