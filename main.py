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
        #Parametrage de fenêtre 
        self.screen.title(nameApp)
        self.screen.iconphoto(True,PhotoImage(file=imagePath))
        self.screen.config(bg=self.configuration.lectureJSON("theme"))
        self.screen.minsize(700,500)
        #Creation du menu 
        topMenu = Menu(self.screen)
        topMenu.add_command(label="Parametre")
        topMenu.add_command(label="Logiciel Arrera")
        topMenu.add_command(label="aide")
        topMenu.add_command(label="A propos",command=self.Apropop)
        #Creation des cadre
        self.mainCadre = Frame(self.screen,bg="red",width=650,height=450)
        self.settingCadre = Frame(self.screen,bg="red",width=650,height=450)
        self.addCadre = Frame(self.screen,bg="red",width=650,height=450)
        self.onlineAddCadre = Frame(self.screen,bg="red",width=650,height=450)
        self.localAddCadre = Frame(self.screen,bg="red",width=650,height=450)
        #Widget mainCadre
        self.btnDoc1 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc2 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc3 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc4 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc5 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc6 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc7 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc8 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc9 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc10 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc11 = Button(self.mainCadre,width="4",height="2")
        self.btnDoc12 = Button(self.mainCadre,width="4",height="2")
        #Affichage 
        self.mainCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.mainAffichage()
        #Ajout de menu a la fenetre
        self.screen.config(menu=topMenu)
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
        
    def mainAffichage(self):
        nbRacoucie=self.configuration.lectureJSON("nbRacoucie")
        nbRacoucie = int(nbRacoucie)
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


ArreraDoc()