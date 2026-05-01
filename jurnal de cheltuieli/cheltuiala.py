class Cheltuiala:
    def __init__(self, descriere, suma, data, categorie):
        self.descriere = descriere
        self.suma = suma
        self.data = data
        self.categorie = categorie

    def __str__(self):
        return f"Cheltuiala: {self.descriere}, suma: {self.suma}, data: {self.data}, categoria: {self.categorie}"
    
    def __eq__(self, other):
        if not isinstance(other, Cheltuiala):
            return False
        return self.descriere == other.descriere and self.suma == other.suma and self.data == other.data and self.categorie == other.categorie
    