
class Voiture:
    
    
    def __init__(self,marque,modele,annee,km=0,en_marche=False,reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    #Les Assesseurs
    def getMarque(self):
        return f"Marque : {self.__marque}"
    
    def getModele(self):
        return f"Modele : {self.__modele}"
    
    def getAnnee(self):
        return f"Annee : {self.__annee}"
    
    def getKm(self):
        return f"Kilometrage : {self.__km}"
    
    def getMarche(self):
        return f"En Marche : {self.__en_marche}"
    
    def __verifier_plein(self):
        return self.__reservoir
    
    #Les Mutateurs
    def setMarque(self,new):
        self.__marque = new

    def setModele(self,new):
        self.__modele = new
        
    def setAnnee(self,new):
        self.__annee = new
        
    def setKm(self,new):
        self.__km = new
        
    def setMarche(self,new):
        self.__en_marche = new
     
    #Les Méthodes   
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.setMarche(True)
    
    def arreter(self):
        self.setMarche(False)
    
    
voiture1 = Voiture("Peugeot","206","12")
print(voiture1.getMarque())
print(voiture1.getModele())
print(voiture1.getAnnee())
print(voiture1.getKm())
print(voiture1.getMarche())
voiture1.demarrer()
print(voiture1.getMarche())
voiture1.arreter()
print(voiture1.getMarche())