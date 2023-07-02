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
        configuration = jsonWork("config.json")
        #Parametrage de fenêtre 
        self.screen.title(nameApp)
        self.screen.iconphoto(True,PhotoImage(file=imagePath))
        self.screen.config(bg=configuration.lectureJSON("theme"))
        self.screen.minsize(700,500)
        #Creation du menu 
        topMenu = Menu(self.screen)
        topMenu.add_command(label="Parametre")
        topMenu.add_command(label="Logiciel Arrera")
        topMenu.add_command(label="aide")
        topMenu.add_command(label="A propos",command=self.Apropop)
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


ArreraDoc()