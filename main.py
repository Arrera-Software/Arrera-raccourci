from tkinter import*
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from objet.ObjetJSON import *
from objet.AddDoc import *

nameApp = "Arrera Documentation"
versionApp = "I2023-1.00.dev07/2023"
imagePath = "image/icon.png"
copyrightApp = "Copyright Arrera Software by Baptiste P 2023-"
class ArreraDoc :
    def __init__(self) :
        #Creation de la fenêtre
        self.screen = Tk()
        #Initialisation du fichier JSON et AddDoc
        self.configuration = jsonWork("config.json")
        self.gestionBTN = AddDoc()
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
        self.topMenu.add_command(label="Logiciel Arrera")
        self.topMenu.add_command(label="aide")
        self.topMenu.add_command(label="A propos",command=self.Apropop)
        #Creation des cadre
        self.mainCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.settingCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.addCadre = Frame(self.screen,bg=color,width=650,height=450)
        self.supprCadre = Frame(self.screen,bg=color,width=650,height=450)
        #Widget mainCadre
        self.btnDoc1 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc2 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc3 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc4 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc5 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc6 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc7 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc8 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc9 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc10 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc11 = Button(self.mainCadre,width="4",height="2",bg=color)
        self.btnDoc12 = Button(self.mainCadre,width="4",height="2",bg=color)
        #widget settingCadre
        self.labelIndication1 = Label(self.settingCadre,text="Nombre de documentation afficher :",bg=color,font=("arial","20"),fg=textColor)
        self.labelIndication2 = Label(self.settingCadre,text="Theme application :",bg=color,font=("arial","20"),fg=textColor)
        self.menuColor = OptionMenu(self.settingCadre,self.varColor,*self.listeColor)
        self.menuApp = OptionMenu(self.settingCadre,self.varNbApp,*self.listNb)
        self.btnValider = Button(self.settingCadre,text="Valider",font=("arial","15"),width="25",bg="green",fg="white",command=self.ecriturePara)
        self.btnAdd = Button(self.settingCadre,text="Ajouter une documentation",font=("arial","15"),width="25",bg=color,fg=textColor,command=self.addPage)
        self.btnSuppr = Button(self.settingCadre,text="Supprimer une documentation",font=("arial","15"),width="25",bg=color,fg=textColor,command=self.supprDoc)
        #widget addCadre
        self.btnOnline = Button(self.addCadre,text="En ligne",bg=color,fg=textColor,font=("arial","15"),command=self.onlineAdd)
        self.btnLocal = Button(self.addCadre,text="Local",bg=color,fg=textColor,font=("arial","15"),command=self.localAdd)
        #widget supprCadre
        self.labelIndication3 = Label(self.supprCadre,text="Choisissez le numero du bouton :",bg=color,font=("arial","20"),fg=textColor)
        self.btnValSuppr = Button(self.supprCadre,text="Supprimer",font=("arial","15"),width="25",bg="red",fg="white")
        #Affichage  
        self.mainAffichage(0)
        #Ajout de menu a la fenetre
        self.screen.config(menu=self.topMenu)
        #Fin de la boucle
        self.screen.mainloop()
    
    def Apropop(self):
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
        self.settingCadre.place_forget()
        self.addCadre.place_forget()
        self.mainCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        nbRacoucie=int(self.configuration.lectureJSON("nbRacoucie"))
        if nbRacoucie !=12 and nbRacoucie !=4 and nbRacoucie !=8:
            self.configuration.EcritureJSON("nbRacoucie","4")
        if nbRacoucie == 12 :
            self.btnDoc1.place(x=35,y=35)
            self.btnDoc2.place(x=185,y=35)
            self.btnDoc3.place(x=427,y=35)
            self.btnDoc4.place(x=577,y=35)
            self.btnDoc5.place(x=35,y=194)
            self.btnDoc6.place(x=185,y=194)
            self.btnDoc7.place(x=427,y=194)
            self.btnDoc8.place(x=577,y=194)
            self.btnDoc9.place(x=35,y=368)
            self.btnDoc10.place(x=185,y=368)
            self.btnDoc11.place(x=427,y=368)
            self.btnDoc12.place(x=577,y=368)
        else :
            if nbRacoucie == 8 :
                self.btnDoc5.place(x=185,y=35)
                self.btnDoc6.place(x=427,y=35)
                self.btnDoc1.place(x=35,y=194)
                self.btnDoc2.place(x=185,y=194)
                self.btnDoc3.place(x=427,y=194)
                self.btnDoc4.place(x=577,y=194)
                self.btnDoc7.place(x=185,y=368)
                self.btnDoc8.place(x=427,y=368)
            else :
                if nbRacoucie == 4:
                    self.btnDoc1.place(x=35,y=194)
                    self.btnDoc2.place(x=185,y=194)
                    self.btnDoc3.place(x=427,y=194)
                    self.btnDoc4.place(x=577,y=194)
        if nb == 1 :
            self.topMenu.entryconfigure("Accueil",label="Parametre",command=self.setting)

    def setting(self):
        self.mainCadre.place_forget()
        self.topMenu.entryconfigure("Parametre",label="Accueil",command=lambda   : self.mainAffichage(1))
        self.settingCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
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
    def ecriturePara(self):
        nb=str(self.varNbApp.get())
        color = str(self.varColor.get())
        self.configuration.EcritureJSON("nbRacoucie",nb)
        self.configuration.EcritureJSON("theme",color)
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
        #Gestion de la couleur des bouton
        self.btnDoc1.configure(bg=color,fg=textColor)
        self.btnDoc2.configure(bg=color,fg=textColor)
        self.btnDoc3.configure(bg=color,fg=textColor)
        self.btnDoc4.configure(bg=color,fg=textColor)
        self.btnDoc5.configure(bg=color,fg=textColor)
        self.btnDoc6.configure(bg=color,fg=textColor)
        self.btnDoc7.configure(bg=color,fg=textColor)
        self.btnDoc8.configure(bg=color,fg=textColor)
        self.btnDoc9.configure(bg=color,fg=textColor)
        self.btnDoc10.configure(bg=color,fg=textColor)
        self.btnDoc11.configure(bg=color,fg=textColor)
        self.btnDoc12.configure(bg=color,fg=textColor)
        self.btnAdd.configure(bg=color,fg=textColor)
        self.btnOnline.configure(bg=color,fg=textColor)
        self.btnLocal.configure(bg=color,fg=textColor)
        #gestion des label
        self.labelIndication1.configure(bg=color,fg=textColor)
        self.labelIndication2.configure(bg=color,fg=textColor)
       
        #Mise a jour de la fenetre
        self.screen.update()
        self.btnDoc1.place_forget()
        self.btnDoc2.place_forget()
        self.btnDoc3.place_forget()
        self.btnDoc4.place_forget()
        self.btnDoc5.place_forget()
        self.btnDoc6.place_forget()
        self.btnDoc7.place_forget()
        self.btnDoc8.place_forget()
        self.btnDoc9.place_forget()
        self.btnDoc10.place_forget()
        self.btnDoc11.place_forget()
        self.btnDoc12.place_forget()
        self.mainAffichage(1)
    
    def addPage(self):
        self.settingCadre.place_forget()
        self.addCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btnOnline.place(x="50",y="194")
        self.btnLocal.place(x="547",y="194")
    
    def textEntryLien(self,event):
        if self.entryLien.get() == "Entrer le lien de la documentation":
            self.entryLien.delete(0, END)
    
    def textEntryName1(self,event):
        if self.entryName1.get() == "Entrez le nom de la doc":
            self.entryName1.delete(0, END)
            self.entryName1.config(foreground="black")
    
    def onlineAdd(self):
        etatBTN = self.gestionBTN.verifEtatBTN()
        for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
            i = str(i)
            if etatBTN[i] == "0":
                nbBTN = str(i)
                break
        self.gestionBTN.AjoutBTN(nbBTN,"web")           
    
    def localAdd(self):
        etatBTN = self.gestionBTN.verifEtatBTN()
        for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
            i = str(i)
            if etatBTN[i] == "0":
                nbBTN = str(i)
                break
        self.gestionBTN.AjoutBTN(nbBTN,"file")
    
    def supprDoc(self):
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
        
ArreraDoc()