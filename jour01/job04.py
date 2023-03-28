from dataclasses import *

@dataclass
class Personne:
    prenom:str ="John"
    nom:str = "Garden"
    
    
    def sePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    

mr1 = Personne()
mr2 = Personne("Jean","Doe")
mr3 = Personne("Pierre")

print(mr1.sePresenter())
print(mr2.sePresenter())
print(mr3.sePresenter())
    