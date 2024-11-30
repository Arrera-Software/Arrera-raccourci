from tkinter import*
from PIL import Image, ImageTk
from objet.ObjetJSON import *
from objet.AddDoc import *
from objet.commandBTN import*

NAMEAPP = "Arrera Raccourci"
VERSIONAPP = "I2024-2.00"
IMAGEPATH = "image/icon.png"
COPYRIGHTAPP = "Copyright Arrera Software by Baptiste P 2023-2024"


class CArreraDoc:
    def __init__(self):
        self.__actionBTNWeb = [
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
        self.__actionBTNFile = [
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
        self.__configuration = jsonWork("config.json")
        self.__gestionBTN = AddDoc()

    def view(self):
        # Creation de la fenêtre
        self.__screen = Tk()
        # Image
        self.__imgDefault = PhotoImage(file="racourcie/img/imgDefault.png")
        # varriable
        color = self.__configuration.lectureJSON("theme")
        if color == "black":
            textColor = "white"
        else:
            textColor = "black"
        self.__varColor = StringVar(self.__screen)
        self.__varNbApp = StringVar(self.__screen)
        self.__varBTN = StringVar(self.__screen)
        # liste
        self.__listeColor = ["white", "black"]
        self.__listNb = ["4", "8", "12"]
        # Parametrage de fenêtre
        self.__screen.title(NAMEAPP)
        self.__screen.iconphoto(True, PhotoImage(file=IMAGEPATH))
        self.__screen.config(bg=color)
        self.__screen.minsize(700, 500)
        # Creation du menu
        self.__topMenu = Menu(self.__screen, bg=color, fg=textColor)
        self.__topMenu.add_command(label="Parametre", command=self.__setting)
        # self.topMenu.add_command(label="Logiciel Arrera",command=lambda : self.arreraDoc(0))
        self.__topMenu.add_command(label="aide", command=lambda: webbrowser.open(
            "https://github.com/Arrera-Software/Arrera-Documentation/blob/main/README.md"))
        self.__topMenu.add_command(label="A propos", command=self.__Apropop)
        # Creation des cadre
        self.__mainCadre = Frame(self.__screen, bg=color, width=650, height=450)
        self.__settingCadre = Frame(self.__screen, bg=color, width=650, height=450)
        self.__addCadre = Frame(self.__screen, bg=color, width=650, height=450)
        self.__supprCadre = Frame(self.__screen, bg=color, width=650, height=450)
        self.__arreraDocCadre = Frame(self.__screen, bg=color, width=650, height=450)
        # Widget mainCadre
        self.__btnDoc = [
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color),
            Button(self.__mainCadre, bg=color)
        ]  # Liste de bouton pour simplifier la gestion
        # widget settingCadre
        self.__labelIndication1 = Label(self.__settingCadre, text="Nombre de raccourcis affichés : ", bg=color,
                                      font=("arial", "20"), fg=textColor)
        self.__labelIndication2 = Label(self.__settingCadre, text="Thème application : ", bg=color, font=("arial", "20"),
                                      fg=textColor)
        self.__menuColor = OptionMenu(self.__settingCadre, self.__varColor, *self.__listeColor)
        self.__menuApp = OptionMenu(self.__settingCadre, self.__varNbApp, *self.__listNb)
        self.__btnValider = Button(self.__settingCadre, text="Valider", font=("arial", "15"), width="25", bg="green",
                                 fg="white", command=self.__ecriturePara)
        self.__btnAdd = Button(self.__settingCadre, text="Ajouter un raccourci", font=("arial", "15"), width="25",
                             bg=color, fg=textColor, command= lambda : self.__addPage())
        self.__btnSuppr = Button(self.__settingCadre, text="Supprimer un raccourci", font=("arial", "15"), width="25",
                               bg=color, fg=textColor, command=lambda : self.__supprDoc())
        self.__btnBack1 = Button(self.__settingCadre, text="Retour Accueil", bg=color, fg=textColor, font=("arial", "15"),
                               width="25", command=lambda: self.__mainAffichage(1))
        # widget addCadre
        self.__btnOnline = Button(self.__addCadre, text="En ligne", bg=color, fg=textColor, font=("arial", "15"),
                                command=self.__onlineAdd)
        self.__btnLocal = Button(self.__addCadre, text="Local", bg=color, fg=textColor, font=("arial", "15"),
                               command=self.__localAdd)
        self.__btnBack2 = Button(self.__addCadre, text="Retour Accueil", bg=color, fg=textColor, font=("arial", "15"),
                               command=lambda: self.__mainAffichage(1))
        # widget supprCadre
        self.__labelIndication3 = Label(self.__supprCadre, text="Choisissez le numéro du bouton :", bg=color,
                                      font=("arial", "20"), fg=textColor)
        self.__btnValSuppr = Button(self.__supprCadre, text="Supprimer", font=("arial", "15"), width="25", bg="red",
                                  fg="white")
        # widget arreraDocCadre
        # Affichage
        self.__mainAffichage(0)
        # Ajout de menu a la fenetre
        self.__screen.config(menu=self.__topMenu)
        # Fin de la boucle
        self.__screen.mainloop()

    def __Apropop(self):  # Fonction fenetre a propos
        # Variable
        tailleIMG = (100, 100)
        # Creation de la fenetre
        about = Toplevel()
        about.title("A propos : " + NAMEAPP)
        about.maxsize(400, 300)
        about.minsize(400, 300)
        about.config(bg="white")
        # Traitement Image
        imageOrigine = Image.open(IMAGEPATH)
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        # Label
        labelIcon = Label(about, bg="white")
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about, text="\n" + NAMEAPP + "\n", font=("arial", "12"), bg="white")
        labelVersion = Label(about, text=VERSIONAPP + "\n", font=("arial", "11"), bg="white")
        labelCopyright = Label(about, text=COPYRIGHTAPP, font=("arial", "9"), bg="white")
        # affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()

    def __mainAffichage(self, nb):
        # Mise en page des bouton
        self.__actulisation()
        # Desafisage de tou les carde
        self.__settingCadre.place_forget()
        self.__addCadre.place_forget()
        self.__supprCadre.place_forget()
        # Affichage du cadre principale
        self.__mainCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        # Recuperation du nombre de bouton de l'interface
        nbRacoucie = int(self.__configuration.lectureJSON("nbRacoucie"))
        # Protection contre les modification du fichier
        if nbRacoucie != 12 and nbRacoucie != 4 and nbRacoucie != 8:
            self.__configuration.EcritureJSON("nbRacoucie", "4")
        # Affichage des bouton btnDoc
        if nbRacoucie == 12:
            self.__btnDoc[8].place(x=35, y=35)
            self.__btnDoc[9].place(x=577, y=35)
            self.__btnDoc[4].place(x=185, y=35)
            self.__btnDoc[5].place(x=427, y=35)
            self.__btnDoc[0].place(x=35, y=194)
            self.__btnDoc[1].place(x=185, y=194)
            self.__btnDoc[2].place(x=427, y=194)
            self.__btnDoc[3].place(x=577, y=194)
            self.__btnDoc[6].place(x=185, y=368)
            self.__btnDoc[7].place(x=427, y=368)
            self.__btnDoc[10].place(x=35, y=368)
            self.__btnDoc[11].place(x=577, y=368)
        else:
            if nbRacoucie == 8:
                self.__btnDoc[4].place(x=185, y=35)
                self.__btnDoc[5].place(x=427, y=35)
                self.__btnDoc[0].place(x=35, y=194)
                self.__btnDoc[1].place(x=185, y=194)
                self.__btnDoc[2].place(x=427, y=194)
                self.__btnDoc[3].place(x=577, y=194)
                self.__btnDoc[6].place(x=185, y=368)
                self.__btnDoc[7].place(x=427, y=368)
            else:
                if nbRacoucie == 4:
                    self.__btnDoc[0].place(x=35, y=194)
                    self.__btnDoc[1].place(x=185, y=194)
                    self.__btnDoc[2].place(x=427, y=194)
                    self.__btnDoc[3].place(x=577, y=194)
        # Remise de Parametre au lieu de aceuil dans le menu superieur
        if nb == 1:
            self.__topMenu.entryconfigure("Accueil", label="Parametre", command=self.__setting)
            # self.topMenu.entryconfigure("Logiciel Arrera",label="Logiciel Arrera",command=lambda : self.arreraDoc(0))

    def __setting(self):
        # Desafichage du cadre principale
        self.__mainCadre.place_forget()
        # Changement du menu supperieur
        self.__topMenu.entryconfigure("Parametre", label="Accueil", command=lambda: self.__mainAffichage(1))
        # self.topMenu.entryconfigure("Logiciel Arrera",label="Logiciel Arrera",command=lambda : self.arreraDoc(1))
        # Affichage du cadte de parametre
        self.__settingCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
        # Affichage des widget
        self.__labelIndication1.place(x="0", y="15")
        self.__labelIndication2.place(x="195", y="75")
        nb = int(self.__configuration.lectureJSON("nbRacoucie"))
        color = self.__configuration.lectureJSON("theme")
        if nb == 4:
            self.__varNbApp.set(self.__listNb[0])
        else:
            if nb == 8:
                self.__varNbApp.set(self.__listNb[1])
            else:
                if nb == 12:
                    self.__varNbApp.set(self.__listNb[2])
        if color == "black":
            self.__varColor.set(self.__listeColor[1])
        else:
            if color == "white":
                self.__varColor.set(self.__listeColor[0])
        self.__menuApp.place(x="440", y="15")
        self.__menuColor.place(x="440", y="75")
        self.__btnValider.place(x="200", y="135")
        self.__btnAdd.place(x="200", y="195")
        self.__btnSuppr.place(x="200", y="255")
        self.__btnBack1.place(x="200", y="315")

    def __ecriturePara(self):
        # Recuperation des valeur
        nb = str(self.__varNbApp.get())
        color = str(self.__varColor.get())
        # ecriture des valeur
        self.__configuration.EcritureJSON("nbRacoucie", nb)
        self.__configuration.EcritureJSON("theme", color)
        # Definition de la couleur des texte
        if color == "black":
            textColor = "white"
        else:
            textColor = "black"
        # Gestion de la fenetre
        self.__screen.configure(bg=color)
        self.__topMenu.configure(bg=color, fg=textColor)
        # Gestion de la couleur des cadre
        self.__mainCadre.configure(bg=color)
        self.__settingCadre.configure(bg=color)
        self.__addCadre.configure(bg=color)
        # Gestion de la couleur des bouton
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            self.__btnDoc[i].configure(bg=color)
        self.__btnAdd.configure(bg=color, fg=textColor)
        self.__btnOnline.configure(bg=color, fg=textColor)
        self.__btnLocal.configure(bg=color, fg=textColor)
        self.__btnSuppr.configure(bg=color, fg=textColor)
        self.__btnBack1.configure(bg=color, fg=textColor)
        self.__btnBack2.configure(bg=color, fg=textColor)
        # gestion des label
        self.__labelIndication1.configure(bg=color, fg=textColor)
        self.__labelIndication2.configure(bg=color, fg=textColor)

        # Mise a jour de la fenetre
        self.__screen.update()
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            self.__btnDoc[i].place_forget()
        self.__mainAffichage(1)

    def __addPage(self):  # Fonction d'ajout de doc
        self.__settingCadre.place_forget()
        nbBTNLibre = self.__gestionBTN.verifNbBTNLibre()
        if nbBTNLibre > 0:
            self.__addCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.__btnBack2.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.__btnOnline.place(x="50", y="205")
            self.__btnLocal.place(x="547", y="205")
        else:
            self.__mainAffichage(1)
            messagebox.showwarning("Attention",
                                   "Vous avez atteint le nombre maximal de raccourcis que vous pouvez rajouter.")

    def __onlineAdd(self):  # Fonction pour les doc en ligne
        nbBTNLibre = self.__gestionBTN.verifNbBTNLibre()
        if nbBTNLibre > 0:
            etatBTN = self.__gestionBTN.verifEtatBTN()
            for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                i = str(i)
                if etatBTN[i] == "0":
                    nbBTN = str(i)
                    self.__gestionBTN.AjoutBTN(nbBTN, "web")
                    break
        else:
            self.__mainAffichage(1)
            messagebox.showwarning("Attention",
                                   "Vous avez atteint le nombre maximal de raccourcis que vous pouvez rajouter.")

    def __localAdd(self):  # Fonction pour les doc local
        nbBTNLibre = self.__gestionBTN.verifNbBTNLibre()
        if nbBTNLibre > 0:
            etatBTN = self.__gestionBTN.verifEtatBTN()
            for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                i = str(i)
                if etatBTN[i] == "0":
                    nbBTN = str(i)
                    self.__gestionBTN.AjoutBTN(nbBTN, "file")
                    break
        else:
            self.__mainAffichage(1)
            messagebox.showwarning("Attention",
                                   "Vous avez attient le nombre maximal de raccourci que vous pouvez rajoutez")

    def __supprDoc(self):  # Fonction de suppression des doc
        listBTNUse = []
        for cles, valeur in self.__gestionBTN.verifEtatBTN().items():
            if valeur == "1":
                listBTNUse.append(str(cles))
        if listBTNUse == []:
            messagebox.showwarning("Attention",
                                   "Vous avez pas supprimer de raccourci si vous nous avez pas ajouter")
        else:
            self.listeBTN = OptionMenu(self.__supprCadre, self.__varBTN, *listBTNUse)

            def suppr():
                self.__gestionBTN.supprBTN(str(self.__varBTN.get()))
                self.__mainAffichage(1)

            self.__settingCadre.place_forget()
            self.__varBTN.set(listBTNUse[0])
            self.__supprCadre.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.__labelIndication3.place(x="0", y="15")
            self.listeBTN.place(x="440", y="15")
            self.__btnValSuppr.configure(command=suppr)
            self.__btnValSuppr.place(x="200", y="135")

    def __noDoc(self):
        messagebox.showwarning("Attention", "Vous n'avez pas rajouter de raccourci sur ce bouton")

    def __actulisation(self):
        etatBTN = self.__gestionBTN.verifEtatBTN()
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            nb = str(i + 1)
            if etatBTN[nb] == "1":
                emplacementIMG = "racourcie/img/imgBTN" + nb + ".png"
                image = PhotoImage(file=emplacementIMG, master=self.__btnDoc[i])
                self.__btnDoc[i].image_names = image
                type = self.__gestionBTN.recuperationType(nb)
                if type == "web":
                    self.__btnDoc[i].configure(image=image, command=self.__actionBTNWeb[i].open)
                else:
                    self.__btnDoc[i].configure(image=image, command=self.__actionBTNFile[i].open)
            else:
                self.__btnDoc[i].configure(image=self.__imgDefault, command=self.__noDoc)