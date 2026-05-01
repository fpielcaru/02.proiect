from proj import Carte

def scrie_in_fisier(carte):  # ← atenție: "scrie", nu "scrise"
    fisier = open("carti.txt", "a")
    fisier.write(str(carte) + "\n")
    fisier.close()

def citeste_din_fisier():
    fisier = open("carti.txt", "r")
    carti = []
    for line in fisier:
        carti.append(line.strip())
    fisier.close()
    return carti

carte1 = Carte("Sa ucizi o pasare cantatoare", "Harper Lee", 1960, "Fiction")

scrie_in_fisier(carte1)  # ← trebuie să se potrivească cu numele de sus
carti = citeste_din_fisier()
for carte in carti:
    print(carte)