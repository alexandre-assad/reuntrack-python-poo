
class Student:
    
    def __init__(self,nom,prenom,id,credit=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credit = credit
        self.__level = self.__studentEval()
        
    def studentinfo(self):
        return f"Prenom :{self.__prenom}\nNom : {self.__nom}\nId : {self.__id}\nLevel :{self.__level}"
    
    def add_credits(self,newcredit:int)->int:
        try:
            if newcredit > 0:
                self.__credit += newcredit
                self.__level = self.__studentEval()
            else:
                print("\nVeuillez choisir un nombre positif")
        except:
            print("\nVeuillez choisir un nombre positif")
        
    def get_credits(self):
        return f"Le nombre de credits de {self.__prenom} {self.__nom} est de {self.__credit} points"
    
    def __studentEval(self):
        if self.__credit >=90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Très bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "Passable"
        else:
            return "Insufisant"
    
eleve1 = Student("Doe","John",145)
print(eleve1.studentinfo())
eleve1.add_credits(10)
eleve1.add_credits(10)
eleve1.add_credits("10")
eleve1.add_credits(10)
print(eleve1.get_credits())
print(eleve1.studentinfo())
eleve1.add_credits(50)
print(eleve1.studentinfo())