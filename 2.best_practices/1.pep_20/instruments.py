# instruments.py

class Guitar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def play(self):
        print(f"Playing a {self.brand} {self.model} guitar!")

    def fender(self, name):
        self.brand = name
        self.model = 'fender'
        self.play()

    def ibanez(self, name):
        self.brand = name
        self.model = 'ibanez'
        self.play()


guitars = Guitar('', '')
