import random
couleurs = ["Pique","Coeur","Trefles","Carreaux"]
valeurs = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]
paquet = []
class Carte: 
#On crée une classe carte, qui sert simplement à représenter une carte
    
    def __init__(self,valeur,couleur):
        self.couleur = couleur
        self.valeur = valeur 
        
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"
        
#Hors de la classe, on génère un paquet de 52 cartes
for color in couleurs:
    for val in valeurs:
        paquet.append(Carte(val,color))
random.shuffle(paquet)
class Jeu:
#La classe jeu, avec les méthodes pour le blackjack
    def __init__(self):
        pass
#Piocher à une main un nombre n de carte, et l'enlever du paquet
    def pioche(self,nombre,main):
        for i in range(nombre):
            alea = random.randint(0,len(paquet))
            main.append(paquet[alea])    
            paquet.remove(paquet[alea]) 
        return main       
#Calculer la valeur d'une main (la difficulté de se programme ainsi que cette fonction est surtout au niveau de l'as, soit 11 soit 1)
    def pointMain(self,main):
        total = 0
        numberAce = 0
        for i in main:
            if i.valeur == "Valet" or i.valeur == "Dame" or i.valeur == "Roi":
                total += 10
            elif i.valeur == "As":
                total += 11
                numberAce += 1
            else:
                total += int(i.valeur)
        while total > 21:
            if numberAce > 0:
                total -= 10
                numberAce -= 1
            else:
                return [total,numberAce]
        return [total,numberAce]
    
#La fonction burn pour savoir si quelqu'un dépasse 21 points
    def burn(self,main):
        global pointCroupier
        point = self.pointMain(main)[0]
        numAce = self.pointMain(main)[1]
        while point > 21:
            if numAce >0:
                point -= 10
                numAce -= 1
            else:
                return True
        return False
            
partie = Jeu()
mainCroupier = []
mainjoueur = []
mainCroupier = partie.pioche(2,mainCroupier)
mainjoueur = partie.pioche(2,mainjoueur)
run = True
fin = False
#La boucle d'une partie de BlackJack
while run:
    action = int(input(f"""
Votre Main : {mainjoueur}

Que Voulez Vous Faire ?                       
(1) Passer
(2) Piocher
"""))
    if action == 2:
        mainjoueur = partie.pioche(1,mainjoueur)
        if partie.burn(mainjoueur):
            print("\nDéfaite ! Vous avez Burn")
            print(f"\n Votre main : {mainjoueur}")
            run = False
    elif action == 1:
        print(f"\n Main du Croupier : {mainCroupier}")
        while partie.pointMain(mainCroupier)[0]<17:
            mainCroupier = partie.pioche(1,mainCroupier)
            if partie.burn(mainCroupier):
                print("\nVictoire ! Le Croupier a Burn")
                fin = True
            print(f"\n Main Croupier : {mainCroupier}")
        if fin == True:
            run = False
        elif partie.pointMain(mainCroupier)[0] >= partie.pointMain(mainjoueur)[0]:
            print("\nDéfaite !")
            run = False
        elif partie.pointMain(mainCroupier)[0] < partie.pointMain(mainjoueur)[0]:
            print("\nVictoire !")
            run = False