class Eveniment:
    def __init__(self, nume, data, locatie, nr_bilete, pret_bilet):
        # Validări
        if not nume or not locatie:
            raise ValueError("Numele și locația nu pot fi goale")
        if nr_bilete < 0:
            raise ValueError("Numărul de bilete nu poate fi negativ")
        if pret_bilet <= 0:
            raise ValueError("Prețul biletului trebuie să fie pozitiv")
        
        self.nume = nume
        self.data = data
        self.locatie = locatie
        self.nr_bilete = nr_bilete
        self.pret_bilet = pret_bilet
    
    def calculeaza_incasari(self):
        return self.nr_bilete * self.pret_bilet
    
    def __str__(self):
        return f"{self.nume} | {self.data} | {self.locatie} | Bilete: {self.nr_bilete} | Încasări: {self.calculeaza_incasari()} lei"
    
    def __eq__(self, other):
        if not isinstance(other, Eveniment):
            return False
        return self.nume == other.nume and self.data == other.data