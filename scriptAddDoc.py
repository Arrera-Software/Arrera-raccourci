#Fichier de test de l'objet addDoc
from objet.AddDoc import*
print("Fichier de test de l'objet addDoc")
objet = AddDoc()
var = 1
while (var != 0):
    print("0.Quitter \n1. verifEtatBTN \n2. motifEtatBTN (True) \n3.motifEtatBTN (False) \n4.AjoutBTN (web) \n5.AjoutBTN(file) \n6.supprBTN")
    var = int(input("§"))
    match var :
        case 1 :
            print(objet.verifEtatBTN())
        case 2 :
            btn = str(input("Entrer numero bouton :"))
            objet.modifEtatBTN(btn,True)
        case 3 :
            btn = str(input("Entrer numero bouton :"))
            objet.modifEtatBTN(btn,False)
        case 4 :
            btn = str(input("Entrer numero bouton :"))
            objet.AjoutBTN(btn,"web")
        case 5 :
            btn = str(input("Entrer numero bouton :"))
            objet.AjoutBTN(btn,"file")
        case 6 :
            btn = str(input("Entrer numero bouton :"))
            objet.supprBTN(btn)
        case other :
            break