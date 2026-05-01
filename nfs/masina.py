class Masina:
    def __init__(self, marca, model, an , cp):
        self.marca = marca
        self.model = model
        self.an = an
        self.cp = cp
    def __str__(self):
        return f"Masina {self.marca} {self.model} din anul {self.an} cu {self.cp} CP"
    