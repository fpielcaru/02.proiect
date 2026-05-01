class Muzeu:
    def __init__(self, nume, adresa, masina, program):
        self.nume = nume
        self.adresa = adresa
        self.masina = masina
        self.program = program
    def __str__(self):
        return f"Muzeul {self.nume} se afla la adresa {self.adresa} si are in colectie masina {self.masina}. Programul de vizitare este {self.program}"
    