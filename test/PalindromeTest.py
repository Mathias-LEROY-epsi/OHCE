import unittest
import parameterized.parameterized

from src.langues.Constantes import Constantes
from src.langues.LangueAnglaise import LangueAnglaise
from src.langues.LangueFrancaise import LangueFrancaise
from src.utilities.LangueSpy import LangueSpy
from src.utilities.OhceBuilder import OhceBuilder


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        # QUAND on saisit une chaîne
        o = OhceBuilder.default()
        result = o.palindrome(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], result)

    @parameterized.parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE],
        [LangueFrancaise(), Constantes.Francais.BIEN_DIT],
    ],
        lambda _, __, args:
        "test ETANT DONNE un utilisateur parlant la langue %s \n"
        "QUAND on saisit un palindrome \n"
        "ALORS %s est renvoyé ensuite"
        % (str(type(args.args[0]).__name__), args.args[1])
    )
    def test_palindrome(self, langue, bien_dit):
        palindrome = "radar"

        o = OhceBuilder().ayant_pour_langue(langue).build()

        result = o.palindrome(palindrome)
        self.assertIn(palindrome, result)

        # ET 'Bien dit' est renvoyé ensuite
        result_apres_palindrome = result[len(palindrome):len(result)]
        self.assertIn(bien_dit, result_apres_palindrome)

    def test_non_palindrome(self):
        spy_langue = LangueSpy()
        ohce = OhceBuilder() \
            .ayant_pour_langue(spy_langue) \
            .build()

        ohce.palindrome("toto")

        self.assertEqual(0, spy_langue.nombre_appels_a_bien_dit)


if __name__ == '__main__':
    unittest.main()
