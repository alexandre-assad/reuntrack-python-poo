class Rectangle:
    
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
        
    def perimetre(self):
        return self.__largeur*2+self.__longeur*2
    
    def surface(self):
        return self.__longeur * self.__largeur
        
    def setLongeur(self,new):
        self.__longeur = new
    
    def setLargeur(self,new):
        self.__largeur = new
    
    def getLongeur(self):
        return (self.__longeur)

    def getLargeur(self):
        return (self.__largeur)
    
class Parallelepipede(Rectangle):
    
    def __init__(self, hauteur,longeur, largeur):
        self.hauteur = hauteur
        Rectangle.__init__(self,longeur,largeur)
        
    def volume(self):
        return self.surface() * self.hauteur
    
    

r1 = Rectangle(2,3)
p1 = Parallelepipede(2,2,3)
print(r1.surface())
print(p1.surface())
print(p1.volume())
        
        