class Operation :
    
    def __init__(self,nombre1=0,nombre2=0):
        self.nombre1:int = nombre1
        self.nombre2:int = nombre2
    
    def __repr__(self):
        return f"Le nombre1 est {self.nombre1} \nLe nombre2 est {self.nombre2}"
    
    def addition(self):
        return self.nombre1 + self.nombre2
    
op1 = Operation(1,4)
print(op1)
print(op1.addition())