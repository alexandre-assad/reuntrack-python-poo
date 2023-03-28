import math

class Forme:
    
    def __init__(self):
        pass
    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    
    def __init__(self,radius):
        self.radius = radius
        
    def aire(self):
        return math.pi * (self.radius**2)
    
    
f1 = Forme()
print(f1.aire())
r1 = Rectangle(5,5)
print(r1.aire())
c1 = Cercle(3)
print(c1.aire())