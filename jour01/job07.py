

class Livre:  
    def __init__(self,titre,auteur,page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page:int = page
        
    def getLivre(self):
        return f"Titre : {self.__titre}\nAuteur : {self.__auteur}\nPages : {self.__page}"
    
    def setTitre(self,newtitre):
        self.__titre = newtitre
        
    def setAuteur(self,newauteur):
        self.__auteur = newauteur
        
    def setPage(self,newpage:int) -> int:
        try:
            if newpage > 0:
                self.__page = newpage
            else:
                print("\nVeuillez choisir un nombre positif\n")
        except:
            print("\nVeuillez choisir un nombre positif\n")

            

livre1 = Livre("Les 3 Mousquetaires","Alexandre Dumas",947)
print(livre1.getLivre())
livre1.setTitre("Alcools")
livre1.setAuteur("Guillaume Apollinaire")
livre1.setPage("e")
livre1.setPage(-10)
livre1.setPage(125)
print(livre1.getLivre())