from allat import Allat
class Emlos(Allat):
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_, szorzet_szine_):
        super().__init__(nev_, faj_, eletkor_, elohely_, meret_)
        self.szorzet_szine = szorzet_szine_

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves, élőhelye {self.elohely}, mérete {self.meret}, szőrzete {self.szorzet_szine}"