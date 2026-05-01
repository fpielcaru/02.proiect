import os 
import pickle
from film import Film

filme = []

if os.path.exists("filme.pickle"):
    with open("filme.pickle", "rb") as f:
        filme = pickle.load(f)
    print(f"\n S-au incarcat {len(filme)} filme din fisierul 'filme.pickle'.")
else: 
    print("\n Nu s-au gasit filme in fisier, incearca sa adaugi cateva filme.")

while True:
    print("Meniu:")
    print("1. Adauga film/serial")
    print("2. Afiseaza filme/seriale")
    print("3. Salveaza filme/seriale")
    print("4. Sterge filme/seriale")
    print("5. Iesire")
    optiune = input("Alege o optiune: ")
    if optiune == "1":
        titlu = input("Titlu: ")
        gen = input("Gen: ")
        durata = input("Durata: ")
        regizor = input("Regizor: ")
        an_aparitie = input("An aparitie: ")
        distributie = input("Distributie: ")
        rating = input("Rating: ")

        film = Film(titlu, gen, durata, regizor, an_aparitie, distributie, rating)
        filme.append(film)
        print("Filmul a fost adaugat cu succes.")

    elif optiune == "2":
        if not filme:
            print("Nu exista filme in lista.")
        else:
            print("\n Filme in lista:")
            for film in filme:
                print(film)

    elif optiune == "3":
        with open("filme.pickle", "wb") as f:
            pickle.dump(filme, f)
            print("Filmele au fost salvate cu succes !")
    
    elif optiune == "4":
        if not filme:
            print("Nu exista filme in lista.")
        elif filme:
            print("\n Filme in lista:")
            for index, film in enumerate(filme):
                print(f"{index + 1}. {film}") 
            index_sters = int(input("Introdu indexul filmului pe care vrei sa-l stergi: ")) - 1
            if 0 <= index_sters < len(filme):
                filme.pop(index_sters)
                print("Filmul a fost sters cu succes !")
            else:
                print("Index invalid.")
    
    else:
        print("La revedere!")
        break
