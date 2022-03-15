class File:

    def __init__(self):
        self.valeurs = []

    def empiler(self, valeur):
        self.valeurs.insert(-len(self.valeurs),valeur)

    def depiler(self):
        if self.valeurs:
            return self.valeurs.pop()

    def estVide(self):
        return self.valeurs == []

    def nbElm(self):
        return len(self.valeurs)

    def __str__(self):
        ch = ''
        for x in self.valeurs:
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
        return ch

p = File()
p.empiler(5)
p.empiler(1)
p.empiler(7)
p.empiler(9)

print(p)

print(p.nbElm())