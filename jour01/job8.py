class Livre:  
    def __init__(self,titre,auteur,page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page:int = page
        self.__disponible = True
        
        
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
            
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            
    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
            
    
livre1 = Livre("Les 3 Mousquetaires","Alexandre Dumas",947)
print(livre1.getLivre())
print(livre1.verification())
livre1.emprunter()
print(livre1.verification())
livre1.rendre()
print(livre1.verification())