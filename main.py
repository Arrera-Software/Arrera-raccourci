from tkinter import*
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from objet.ObjetJSON import *

nameApp = "Arrera Documentation"
versionApp = "I2023-1.00.dev07/2023"
imagePath = "image/icon.png"
copyrightApp = "Copyright Arrera Software by Baptiste P 2023-"
class ArreraDoc :
    def __init__(self) :
        #Creation de la fenêtre
        self.screen = Tk()
        #Initialisation du fichier JSON
        self.configuration = jsonWork("config.json")
        #varriable
        color = self.configuration.lectureJSON("theme")
        if color == "black":
            textColor = "white"
        else :
            textColor="black"
        self.varColor = StringVar(self.screen)
        self.varNbApp = StringVar(self.screen)
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
        self.addCadre = Frame(self.screen,bg="red",width=650,height=450)
        self.onlineAddCadre = Frame(self.screen,bg="red",width=650,height=450)
        self.localAddCadre = Frame(self.screen,bg="red",width=650,height=450)
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
        self.btnAdd = Button(self.settingCadre,text="Ajouter une documentation",font=("arial","15"),width="25",bg=color,fg=textColor)
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
        self.onlineAddCadre.place_forget()
        self.localAddCadre.place_forget()
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
                self.btnDoc2.place(x=185,y=35)
                self.btnDoc3.place(x=427,y=35)
                self.btnDoc5.place(x=35,y=194)
                self.btnDoc6.place(x=185,y=194)
                self.btnDoc7.place(x=427,y=194)
                self.btnDoc8.place(x=577,y=194)
                self.btnDoc10.place(x=185,y=368)
                self.btnDoc11.place(x=427,y=368)
            else :
                if nbRacoucie == 4:
                    self.btnDoc5.place(x=35,y=194)
                    self.btnDoc6.place(x=185,y=194)
                    self.btnDoc7.place(x=427,y=194)
                    self.btnDoc8.place(x=577,y=194)
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
        
    def ecriturePara(self):
        nb=str(self.varNbApp.get())
        color = str(self.varColor.get())
        self.configuration.EcritureJSON("nbRacoucie",nb)
        self.configuration.EcritureJSON("theme",color)
        if color == "black":
            textColor = "white"
        else :
            textColor="black"
        self.screen.configure(bg=color)
        self.mainCadre.configure(bg=color)
        self.settingCadre.configure(bg=color)
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
        self.labelIndication1.configure(bg=color,fg=textColor)
        self.labelIndication2.configure(bg=color,fg=textColor)
        self.btnAdd.configure(bg=color,fg=textColor)
        
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
        
        
        
ArreraDoc()