from muzeu import Muzeu
import os 

def scrie_in_fisier(muzeu):
    with open("muzeu.txt", "a") as f:
        f.write(str(muzeu))

def citeste_din_fisier():
    if not os.path.exists("muzeu.txt"):
        with open("muze.txt", "w") as f:
            pass

    with open("magazin.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

produs1 = Muzeu("Tiriac Auto", "Str. Otopeni 176", "Nissan GTR Skyline R34", "08:00 | 20:00")
produs2 = Muzeu("RTG", "Str. Aviatiei 786", "Toyota Supra MK4", "10:00 | 20:00" )

scrie_in_fisier(produs1)
scrie_in_fisier(produs2)

muzeu = citeste_din_fisier()
for m in muzeu:
    print(m)