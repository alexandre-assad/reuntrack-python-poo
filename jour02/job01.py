
class Personne:
    
    def __init__(self,age=14):
        self.age:int = age
    
    def afficherAge(self):
        print(self.age)
    
    def modifierAge(self,new):
        self.age = new
        
    def bonjour(self):
        print("Hello")
        
class Eleve(Personne):
    
    def __init__(self, age):
        Personne.__init__(self,age)
    
    def allerEnCours(self):
        print("Je vais à l'école ! ")
        
    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    
    def __init__(self, age, matiere):
        Personne.__init__(self,age)
        self.__matiereEnseignée = matiere
        
    def enseigner(self):
        print(f"Le cours de {self.__matiereEnseignée} va commencer !")
        
        
personne1 = Personne()
eleve1 = Eleve(12)
prof1 = Professeur(41,"Math")
personne1.afficherAge()
eleve1.afficherAge()
prof1.afficherAge()
prof1.enseigner()