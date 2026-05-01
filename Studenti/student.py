class Student:
    def __init__(self, nume, varsta, nota_medie, clasa):
        self.nume = nume
        self.varsta = varsta
        self.nota_medie = nota_medie
        self.clasa = clasa
    
    def __str__(self):
        return f"Numele: {self.nume}, varsta: {self.varsta}, clasa elevului: {self.clasa}, nota medie este de: {self.nota_medie}"
    