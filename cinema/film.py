class Film:
    def __init__(self, titlu, gen, durata, regizor, an_aparitie, distributie, rating):
        self.titlu = titlu
        self.gen = gen
        self.durata = durata
        self.regizor = regizor 
        self.an_aparitie = an_aparitie 
        self.distributie = distributie
        self.rating = None 

    def __str__(self):
        return f" Titlu: {self.titlu}, gen: {self.gen}, durata: {self.durata}, regizor: {self.regizor}, an: {self.an_aparitie}, distributie: {self.distributie}, rating: {self.rating}"
    
    