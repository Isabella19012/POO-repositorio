class Bingo:
    def __init__(self, numBolas, bolas):
        self.set_numBolas(numBolas)
        self.set_bolas(bolas)
    def set_numBolas(self, nb):
        if nb < 0: self.__numBolas = nb
        else: raise ValueError("Número maior que zero")
    def set_bolas(self, nb):
        if nb < 0: self.__bolas = nb
        else: raise ValueError("Número maior que zero")
    def get_bolas(self):
        return self.__bolas
    def get_numBolas(self):
        return self.__numBolas