
class Animal:
    def __init__(self,age=0,prenom= ""):
        self.age = age
        self.prenom = prenom
    
    def __repr__(self):
        return f"L'animal {self.prenom} de {self.age} ans"
        
    def vieillir(self):
        self.age += 1
        return f"L'âge de l'animal {self.age} ans"

    def nommer(self,newPrenom):
        self.prenom = newPrenom
        return f"L'animal se nomme {self.prenom}"
    
dog = Animal()
print(dog.age)
print(dog.vieillir())
print(dog.nommer("Luna"))
print(dog)