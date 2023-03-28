
class Vehicule:
    
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\nPrix : {self.prix}")
        
    def demarrer(self):
        print("Attention je roule !")
        
class Voiture(Vehicule):
    
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
        
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\nPrix : {self.prix}\nNombre de porte : {self.portes}\n")

    def demarrer(self):
        print("Vroum .... !")
        
class Moto(Vehicule):
    
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2
        
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\nPrix : {self.prix}\nNombre de roue : {self.roue}\n")

    def demarrer(self):
        print("GrenADE !!!!!")
        
voiture1 = Voiture("Peugeot","206","2009","4500")
voiture1.informationsVehicule()
moto1 = Moto("Yamaha","540-C","2017","95000")
moto1.informationsVehicule()
voiture1.demarrer()
moto1.demarrer()