from tkinter import*
from PIL import Image, ImageTk
from objet.ObjetJSON import *
from objet.AddDoc import *
from objet.commandBTN import*

nameApp = "Arrera Documentation"
versionApp = "I2023-1.00.dev07/2023"
imagePath = "image/icon.png"
copyrightApp = "Copyright Arrera Software by Baptiste P 2023-"
class ArreraDoc :
    def __init__(self) :
        #Creation de la fenêtre
        self.screen = Tk()
        #Initialisation du fichier JSON , AddDoc ,commandBTN et openPDF
        self.configuration = jsonWork("config.json")
        self.gestionBTN = AddDoc()
        self.actionBTNWeb = [
            CommandWeb("1"),
            CommandWeb("2"),
            CommandWeb("3"),
            CommandWeb("4"),
            CommandWeb("5"),
            CommandWeb("6"),
            CommandWeb("7"),
            CommandWeb("8"),
            CommandWeb("9"),
            CommandWeb("10"),
            CommandWeb("11"),
            CommandWeb("12")
        ]
        self.actionBTNFile = [
            CommandFile("1"),
            CommandFile("2"),
            CommandFile("3"),
            CommandFile("4"),
            CommandFile("5"),
            CommandFile("6"),
            CommandFile("7"),
            CommandFile("8"),
            CommandFile("9"),
            CommandFile("10"),
            CommandFile("11"),
            CommandFile("12")
        ]
        #Documentation
        documentionRyley = openPDF("racourcie/fichier/ryley.pdf")
        #Image
        self.imgDefault = PhotoImage(file="image/imgDefault.png")
        #varriable
        color = self.configuration.lectureJSON("theme")
        if color == "black":
            textColor = "white"
        else :
            textColor="black"
        self.varColor = StringVar(self.screen)
        self.varNbApp = StringVar(self.screen)
        self.varBTN = StringVar(self.screen)
        #liste
        self.listeColor = ["white","black"]
        self.listNb = ["4","8","12"]
        #Parametrage de fenêtre 
        self.screen.title(nameApp)
        self.screen.iconphoto(True,PhotoImage(file=imagePath))
        self.screen.config(bg=color)
        self.screen.minsize(700,500)
        #Creation du menu 
        self.topMenu = Menu(self.screen)
        self.topMenu.add_command(label="Parametre",command=self.setting)
        self.topMenu.add_command(label="Logiciel Arrera",command=lambda : self.arreraDoc(0))
        self.topMenu.add_command(label="aide",command=lambda : webbrowser.open("https://github.com/Arrera-Software/Arrera-Documentation/blob/main/README.md"))
        self.topMenu.add_command(label="A propos",command=self.Apropop)
        #Creation des cadre
        self.mainCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.settingCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.addCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.supprCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.arreraDocCadre = Frame(self.screen,bg=color,width=650,height=450)
        #Widget mainCadre
        self.btnDoc = [
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color),
            Button(self.mainCadre,bg=color)
        ]#Liste de bouton pour simplifier la gestion
        #widget settingCadre
        self.labelIndication1 = Label(self.settingCadre,text="Nombre de documentation afficher :",bg=color,font=("arial","20"),fg=textColor)
        self.labelIndication2 = Label(self.settingCadre,text="Theme application :",bg=color,font=("arial","20"),fg=textColor)
        self.menuColor = OptionMenu(self.settingCadre,self.varColor,*self.listeColor)
        self.menuApp = OptionMenu(self.settingCadre,self.varNbApp,*self.listNb)
        self.btnValider = Button(self.settingCadre,text="Valider",font=("arial","15"),width="25",bg="green",fg="white",command=self.ecriturePara)
        self.btnAdd = Button(self.settingCadre,text="Ajouter une documentation",font=("arial","15"),width="25",bg=color,fg=textColor,command=self.addPage)
        self.btnSuppr = Button(self.settingCadre,text="Supprimer une documentation",font=("arial","15"),width="25",bg=color,fg=textColor,command=self.supprDoc)
        self.btnBack1 = Button(self.settingCadre,text="Retour Acceuil",bg=color,fg=textColor,font=("arial","15"),width="25",command= lambda : self.mainAffichage(1))
        #widget addCadre
        self.btnOnline = Button(self.addCadre,text="En ligne",bg=color,fg=textColor,font=("arial","15"),command=self.onlineAdd)
        self.btnLocal = Button(self.addCadre,text="Local",bg=color,fg=textColor,font=("arial","15"),command=self.localAdd)
        self.btnBack2 = Button(self.addCadre,text="Retour Acceuil",bg=color,fg=textColor,font=("arial","15"),command= lambda : self.mainAffichage(1))
        #widget supprCadre
        self.labelIndication3 = Label(self.supprCadre,text="Choisissez le numero du bouton :",bg=color,font=("arial","20"),fg=textColor)
        self.btnValSuppr = Button(self.supprCadre,text="Supprimer",font=("arial","15"),width="25",bg="red",fg="white")
        #widget arreraDocCadre
        self.btnArreraDoc = [
            Button(self.arreraDocCadre,bg=color,command=documentionRyley.open),#Bouton ryley
            Button(self.arreraDocCadre,bg=color),#Bouton Six
            Button(self.arreraDocCadre,bg=color),#Bouton Arrera Video Download
            Button(self.arreraDocCadre,bg=color),#Bouton Arrera Interface
            Button(self.arreraDocCadre,bg=color),#Bouton arrera info
            Button(self.arreraDocCadre,bg=color)#Bouton arrera copilote
        ]
        #Image btnArreraDoc
        self.imgArreraDoc = [
            PhotoImage(file="racourcie/img/ryley.png",master=self.btnArreraDoc[0]),
            PhotoImage(file="racourcie/img/six.png",master=self.btnArreraDoc[1]),
            PhotoImage(file="racourcie/img/arreraVideoDownload.png",master=self.btnArreraDoc[2]),
            PhotoImage(file="racourcie/img/arreraInterface.png",master=self.btnArreraDoc[3]),
            PhotoImage(file="racourcie/img/arreraInfo.png",master=self.btnArreraDoc[4]),
            PhotoImage(file="racourcie/img/arreraCopilote.png",master=self.btnArreraDoc[5])
        ]
        #Application de image
        for i in [0,1,2,3,4,5]:
            self.btnArreraDoc[i].image_names = self.imgArreraDoc[i]
            self.btnArreraDoc[i].configure(image=self.imgArreraDoc[i])
        #Affichage  
        self.mainAffichage(0)
        #Ajout de menu a la fenetre
        self.screen.config(menu=self.topMenu)
        #Fin de la boucle
        self.screen.mainloop()
    
    def Apropop(self):#Fonction fenetre a propos
        #Variable
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Toplevel()
        about.title("A propos : "+nameApp)
        about.maxsize(400,300)
        about.minsize(400,300)
        about.config(bg="white")
        #Traitement Image
        imageOrigine = Image.open(imagePath)
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,bg="white")
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about,text="\n"+nameApp+"\n",font=("arial","12"),bg="white")
        labelVersion = Label(about,text=versionApp+"\n",font=("arial","11"),bg="white")
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg="white")
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        
    def mainAffichage(self,nb):
        #Mise en page des bouton 
        self.actulisation()
        #Desafisage de tou les carde
        self.settingCadre.place_forget()
        self.addCadre.place_forget()
        self.supprCadre.place_forget()
        self.arreraDocCadre.place_forget()
        #Affichage du cadre principale
        self.mainCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Recuperation du nombre de bouton de l'interface
        nbRacoucie=int(self.configuration.lectureJSON("nbRacoucie"))
        #Protection contre les modification du fichier 
        if nbRacoucie !=12 and nbRacoucie !=4 and nbRacoucie !=8:
            self.configuration.EcritureJSON("nbRacoucie","4")
        #Affichage des bouton btnDoc
        if nbRacoucie == 12 :
            self.btnDoc[8].place(x=35,y=35)
            self.btnDoc[9].place(x=577,y=35)
            self.btnDoc[4].place(x=185,y=35)
            self.btnDoc[5].place(x=427,y=35)
            self.btnDoc[0].place(x=35,y=194)
            self.btnDoc[1].place(x=185,y=194)
            self.btnDoc[2].place(x=427,y=194)
            self.btnDoc[3].place(x=577,y=194)
            self.btnDoc[6].place(x=185,y=368)
            self.btnDoc[7].place(x=427,y=368)
            self.btnDoc[10].place(x=35,y=368)
            self.btnDoc[11].place(x=577,y=368)
        else :
            if nbRacoucie == 8 :
                self.btnDoc[4].place(x=185,y=35)
                self.btnDoc[5].place(x=427,y=35)
                self.btnDoc[0].place(x=35,y=194)
                self.btnDoc[1].place(x=185,y=194)
                self.btnDoc[2].place(x=427,y=194)
                self.btnDoc[3].place(x=577,y=194)
                self.btnDoc[6].place(x=185,y=368)
                self.btnDoc[7].place(x=427,y=368)
            else :
                if nbRacoucie == 4:
                    self.btnDoc[0].place(x=35,y=194)
                    self.btnDoc[1].place(x=185,y=194)
                    self.btnDoc[2].place(x=427,y=194)
                    self.btnDoc[3].place(x=577,y=194)
        #Remise de Parametre au lieu de aceuil dans le menu superieur
        if nb == 1 :
            self.topMenu.entryconfigure("Accueil",label="Parametre",command=self.setting)
            self.topMenu.entryconfigure("Logiciel Arrera",label="Logiciel Arrera",command=lambda : self.arreraDoc(0))

    def setting(self):
        #Desafichage du cadre principale
        self.mainCadre.place_forget()
        #Changement du menu supperieur
        self.topMenu.entryconfigure("Parametre",label="Accueil",command=lambda   : self.mainAffichage(1))
        self.topMenu.entryconfigure("Logiciel Arrera",label="Logiciel Arrera",command=lambda : self.arreraDoc(1))
        #Affichage du cadte de parametre
        self.settingCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Affichage des widget
        self.labelIndication1.place(x="0",y="15")
        self.labelIndication2.place(x="195",y="75")
        nb = int(self.configuration.lectureJSON("nbRacoucie"))
        color = self.configuration.lectureJSON("theme")
        if nb == 4 :
            self.varNbApp.set(self.listNb[0])
        else :
            if nb == 8 :
                self.varNbApp.set(self.listNb[1])
            else :
                if nb == 12 :
                    self.varNbApp.set(self.listNb[2])
        if color == "black":
            self.varColor.set(self.listeColor[1])
        else :
            if color == "white":
                self.varColor.set(self.listeColor[0])
        self.menuApp.place(x="440",y="15")
        self.menuColor.place(x="440",y="75")
        self.btnValider.place(x="200",y="135")
        self.btnAdd.place(x="200",y="195")
        self.btnSuppr.place(x="200",y="255")
        self.btnBack1.place(x="200",y="315")
    
    def ecriturePara(self):
        #Recuperation des valeur
        nb=str(self.varNbApp.get())
        color = str(self.varColor.get())
        #ecriture des valeur
        self.configuration.EcritureJSON("nbRacoucie",nb)
        self.configuration.EcritureJSON("theme",color)
        #Definition de la couleur des texte
        if color == "black":
            textColor = "white"
        else :
            textColor="black"
        #Gestion de la fenetre   
        self.screen.configure(bg=color)
        #Gestion de la couleur des cadre
        self.mainCadre.configure(bg=color)
        self.settingCadre.configure(bg=color)
        self.addCadre.configure(bg=color)
        self.arreraDocCadre.configure(bg=color)
        #Gestion de la couleur des bouton
        for i in [0,1,2,3,4,5,6,7,8,9,10,11] :
            self.btnDoc[i].configure(bg=color)
        self.btnAdd.configure(bg=color,fg=textColor)
        self.btnOnline.configure(bg=color,fg=textColor)
        self.btnLocal.configure(bg=color,fg=textColor)
        self.btnSuppr.configure(bg=color,fg=textColor)
        self.btnBack1.configure(bg=color,fg=textColor)
        self.btnBack2.configure(bg=color,fg=textColor)
        #gestion des label
        self.labelIndication1.configure(bg=color,fg=textColor)
        self.labelIndication2.configure(bg=color,fg=textColor)
       
        #Mise a jour de la fenetre
        self.screen.update()
        for i in [0,1,2,3,4,5,6,7,8,9,10,11] :
            self.btnDoc[i].place_forget()
        self.mainAffichage(1)
    
    def addPage(self):#Fonction d'ajout de doc
        self.settingCadre.place_forget()
        nbBTNLibre = self.gestionBTN.verifNbBTNLibre()
        if nbBTNLibre > 0 :
            self.addCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.btnBack2.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.btnOnline.place(x="50",y="205")
            self.btnLocal.place(x="547",y="205")
        else :
            self.mainAffichage(1) 
            messagebox.showwarning("Attention", "Vous avez attient le nombre maximal de documentation que vous pouvez rajoutez") 
    
    
    def onlineAdd(self):#Fonction pour les doc en ligne
        nbBTNLibre = self.gestionBTN.verifNbBTNLibre()
        if nbBTNLibre > 0 :
            etatBTN = self.gestionBTN.verifEtatBTN()
            for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
                i = str(i)
                if etatBTN[i] == "0":
                    nbBTN = str(i)
                    self.gestionBTN.AjoutBTN(nbBTN,"web")
                    break
        else :
            self.mainAffichage(1) 
            messagebox.showwarning("Attention", "Vous avez attient le nombre maximal de documentation que vous pouvez rajoutez")
        
               
    def localAdd(self):#Fonction pour les doc local
        nbBTNLibre = self.gestionBTN.verifNbBTNLibre()
        if nbBTNLibre > 0 :
            etatBTN = self.gestionBTN.verifEtatBTN()
            for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
                i = str(i)
                if etatBTN[i] == "0":
                    nbBTN = str(i)
                    self.gestionBTN.AjoutBTN(nbBTN,"file")
                    break
        else :
            self.mainAffichage(1) 
            messagebox.showwarning("Attention", "Vous avez attient le nombre maximal de documentation que vous pouvez rajoutez")
        
        
    def supprDoc(self):#Fonction de suppression des doc
        listBTNUse = []
        for cles, valeur in self.gestionBTN.verifEtatBTN().items():
            if valeur == "1":
                listBTNUse.append(str(cles))
        if listBTNUse == [] :
            messagebox.showwarning("Attention", "Vous avez pas supprimer de documentation si vous nous avez pas ajouter")
        else :
            self.listeBTN = OptionMenu(self.supprCadre,self.varBTN,*listBTNUse)
            def suppr():
                self.gestionBTN.supprBTN(str(self.varBTN.get()))
                self.mainAffichage(1)
            self.settingCadre.place_forget()
            self.varBTN.set(listBTNUse[0])
            self.supprCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.labelIndication3.place(x="0",y="15")
            self.listeBTN.place(x="440",y="15")
            self.btnValSuppr.configure(command=suppr)
            self.btnValSuppr.place(x="200",y="135")
    
    def noDoc(self):
        messagebox.showwarning("Attention", "Vous n'avez pas rajouter de documentation sur ce bouton")
    
    def actulisation(self):
        etatBTN = self.gestionBTN.verifEtatBTN()
        for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
            nb = str(i+1)
            if etatBTN[nb] == "1" :
                emplacementIMG = "racourcie/img/imgBTN"+nb+".png"
                image = PhotoImage(file=emplacementIMG,master=self.btnDoc[i])
                self.btnDoc[i].image_names = image
                type = self.gestionBTN.recuperationType(nb)
                if type == "web":
                    self.btnDoc[i].configure(image=image,command = self.actionBTNWeb[i].open)
                else :
                    self.btnDoc[i].configure(image=image,command= self.actionBTNFile[i].open)
            else :
                self.btnDoc[i].configure(image=self.imgDefault,command=self.noDoc)
    
    def arreraDoc(self,para:int):
        #Desafisage des cadre
        self.settingCadre.place_forget()
        self.addCadre.place_forget()
        self.supprCadre.place_forget()
        self.mainCadre.place_forget()
        #Affichage du cadre principale
        self.arreraDocCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Changement du bouton du menu
        self.topMenu.entryconfigure("Logiciel Arrera",label="Logiciel Arrera",command=lambda : self.arreraDoc(1))
        if para == 0:
            self.topMenu.entryconfigure("Parametre",label="Accueil",command=lambda   : self.mainAffichage(1))
        #Affichage widget
        self.btnArreraDoc[0].place(x=5,y=194)
        self.btnArreraDoc[1].place(x=105,y=194)
        self.btnArreraDoc[2].place(x=205,y=194)
        self.btnArreraDoc[3].place(x=395,y=194)
        self.btnArreraDoc[4].place(x=495,y=194)
        self.btnArreraDoc[5].place(x=595,y=194)
        
ArreraDoc()