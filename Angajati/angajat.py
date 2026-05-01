class Angajat:
    def __init__(self, nume, functie, salariu, vechime):
        self.nume = nume 
        self.functie = functie
        self.salariu = salariu
        self.vechime = vechime

    def __str__(self):
        return f"{self.nume}, {self.functie}, {self.salariu}, {self.vechime}"