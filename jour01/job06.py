

class Rectangle:
    
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
        
    def getDimension(self):
        return f"Longeur : {self.__longeur}\n Largeur : {self.__largeur}"
    
    def setLongeur(self,longeur):
        self.__longeur = longeur
        
    def setLargeur(self,largeur):
        self.__largeur = largeur
        
r1 = Rectangle(10,5)
print(r1.getDimension())
r1.setLongeur(7)
r1.setLargeur(6)
print(r1.getDimension())