class Ohce:
    def __init__(self, langue, periode_journee):
        self.__periode_journee = periode_journee
        self.__langue = langue

    def palindrome(self, palindrome):
        palindrome = palindrome.strip()
        miroir = palindrome[::-1]
        if palindrome == miroir:
            return palindrome + ', ' + self.__langue.bien_dit()
        else:
            return miroir

    def dire_bonjour(self):
        return self.__langue.salutation(self.__periode_journee)

    def dire_au_revoir(self):
        return self.__langue.dire_au_revoir(self.__periode_journee)
