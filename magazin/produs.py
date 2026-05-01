class Produs:
    def __init__(self, nume, categorii, pret, stoc):
        self.nume = nume
        self.categorii = categorii
        self.pret = pret
        self.stoc = stoc

    def __str__(self):
        return f"Produs: {self.nume}, categorie: {self.categorii}, pret: {self.pret}, stoc: {self.stoc}"