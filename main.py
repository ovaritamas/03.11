from allat import *
from emlos import *

allat_1 = Allat("Bodri", "kutya", 3, "ház", "közepes")
allat_2 = Allat("Cirmi", "macska", 2, "ház", "kicsi")

emlos = Emlos("Morzsi", "kutya", 3, "ház", "közepes", "barna")

print(allat_1)
print(allat_2)
print(emlos)

morzsi = Kutya("Morzsi", 5, "ház", "barna")
hubert = Macska("Hubert", 2, "ház", "fekete")
madar = Madar("Rikárdó")
keteltu = Keteltu("Adolf")
hullo = Hullo("János")

madar.csiripel()
keteltu.brekeg()
hullo.napozik_a_kovon()
