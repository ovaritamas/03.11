class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves, élőhelye {self.elohely}"
    
class Madar(Allat):
    def __init__(self, nev_):
        super().__init__(nev_, "madár", 1, "erdő", "kicsi")

    def csiripel(self):
        print(f"{self.nev} csiripel...")
        
class Keteltu(Allat):
    def __init__(self, nev_):
        super().__init__(nev_, "keteltu", 2, "tópart", "kicsi")

    def brekeg(self):
        print(f"{self.nev} brekeg...")

class Hullo(Allat):
    def __init__(self, nev_):
        super().__init__(nev_, "hullo", 3, "szikla", "kicsi")

    def napozik_a_kovon(self):
        print(f"{self.nev} napozik a kövön...")