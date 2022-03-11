class Voiture:
    #methode d'envoi de email: SMTP
    voiture_creer=0
    #initialiser des instances, le sel peut etre remplacer par n'importe quoi
    def __init__(self, marque):
        #Voiture.voiture_creer+=1
        self.marque=marque

    #exlication de self
    # def afficher_marque(self):
    #     print(f"la voiture est de marque: {self.marque}")
voiture_01=Voiture("BMW")
#voiture_02=Voiture("Volvo")

#print(Voiture.voiture_creer)
voiture_01.afficher_marque()
