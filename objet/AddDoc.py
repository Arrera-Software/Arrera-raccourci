#Module python
import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image

#Fichier
from objet.ObjetJSON import *


class AddDoc :
    def __init__(self):
        self.etatBTN = jsonWork("racourcie/etatBtn.json")
        
    def verifEtatBTN(self):
        dictSortie = {"1":"",
                      "2":"",
                      "3":"",
                      "4":"",
                      "5":"",
                      "6":"",
                      "7":"",
                      "8":"",
                      "9":"",
                      "10":"",
                      "11":"",
                      "12":"",
                      }
        for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
            dictSortie[str(i)] = self.etatBTN.lectureJSON(str(i))
        
        return dictSortie

    
    def modifEtatBTN(self,nbBTN:str,etat:bool):
        if etat == True:
            #Si etat est egal a true 
            self.etatBTN.EcritureJSON(nbBTN,"1")
            #On ecrit la valeur 1 au bouton choisi 
        else :
            #si etat est egal a false 
            self.etatBTN.EcritureJSON(nbBTN,"0")
            #On ecrit la valeur 0 au bouton choisi
            
            
    def AjoutBTN(self,nbBTN : str,typeLien : str):#Fonction qui permet de rajouter les lien des doc est une image au bouton
        nbBTN = str(nbBTN)
        if self.etatBTN.lectureJSON(nbBTN) != "1" and typeLien != "web" or typeLien != "file" :
            #Creation de l'objet json
            fichierBTN = jsonWork("racourcie/configBTN/btnDoc"+nbBTN+".json")
            #Fentre d'avertisement
            messagebox.showwarning("Attention", "Dans la fenêtre suivante, veuillez sélectionner une image au format .png")
            #Recuperation de l'image et redimentionement et renomage
            icone = Image.open(askopenfilename(defaultextension=".png", filetypes=[("Image", ".png")]))
            newIcone = icone.resize((50,50))
            newIcone.save("racourcie/img/imgBTN"+nbBTN+".png")
            #Ajout des doc
            if typeLien == "file" :#Si file
                #Fentre d'avertisement
                messagebox.showwarning("Attention", "Dans la fenêtre suivante, veuillez sélectionner une documentation au format pdf")
                #Recuperation du fichier
                source = askopenfilename(defaultextension=".png", filetypes=[("Image", ".pdf")])
                #Copie
                shutil.copy2(source,"racourcie/fichier")
                #Renomage
                newFileName = os.path.join("racourcie/fichier","doc"+nbBTN+".pdf")
                os.rename(os.path.join("racourcie/fichier", os.path.basename(source)),newFileName)
                #Enregistrement dans le fichier json du type
                fichierBTN.EcritureJSON("type","file")
                self.modifEtatBTN(nbBTN,True)
            else :#Si web
                #Fentre d'avertisement
                messagebox.showwarning("Attention", "Dans la fenêtre suivante, veuillez entrer le lien internet de la documentation")
                #Creation fenetre de recuperation
                screen = Tk()
                screen.title("Ajout lien")
                screen.maxsize(300,100)
                screen.minsize(300,100)  
                screen.configure(bg="white")
                entryLien = Entry(screen,width=10,font=("arial","15"))
                entryLien.pack()
                def wirte():
                    #Recuperation de lien est ecriture dans le fichier json
                    fichierBTN.EcritureJSON("lien",entryLien.get())
                    #Ecriture du type web dans le fichier json
                    fichierBTN.EcritureJSON("type","web")
                    self.modifEtatBTN(nbBTN,True)
                    screen.destroy()
                    
                Button(screen,text="Valider",bg="white",font=("arial","15"),command=wirte).pack()
                screen.mainloop()
            #Passage du bouton en utiliser
            return True
        else :
            return False
            
    def supprBTN(self,nbBTN):
        nbBTN = str(nbBTN)
        if self.etatBTN.lectureJSON(nbBTN) == "1":
            #Overture du fichier bouton
            fichierBTN = jsonWork("racourcie/configBTN/btnDoc"+nbBTN+".json")
            #Suppression de l'image 
            os.remove("racourcie/img/imgBTN"+nbBTN+".png")
            if fichierBTN.lectureJSON("type") == "file" :#Si le bouton est associer a un fichier
                #Suppression d'un du ficher pdf
                os.remove("racourcie/fichier/doc"+nbBTN+".pdf")
                #Reset du type
                fichierBTN.EcritureJSON("type","")
            else :#Si le bouton est associer a un site web
                #Suppression du lien
                fichierBTN.EcritureJSON("lien","")
                #Reset du type
                fichierBTN.EcritureJSON("type","")
            #Modification de l'etat du bouton
            self.modifEtatBTN(nbBTN,False)
            return True
        else :
            return False
        
        
    def recuperationType(self,nbBTN):
        var = jsonWork("racourcie/configBTN/btnDoc"+str(nbBTN)+"json").lectureJSON("type")
        return  var
    
    def recuperationType(self,nbBTN):
        return jsonWork("racourcie/configBTN/btnDoc"+str(nbBTN)+"json").lectureJSON("lien")
    