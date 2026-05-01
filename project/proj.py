class Carte:
    def __init__(self, title, author, publicated_year, genre):
        self.title = title
        self.author = author
        self.publicated_year = publicated_year
        self.genre = genre
    
    def __str__(self):
        return f"{self.title} by {self.author}, publicated in {self.publicated_year}, genre: {self.genre}"
    