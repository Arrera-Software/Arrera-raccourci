from tkinter import*
import webbrowser
#Varriable
Color = "#3c0f14"
TextColor = "white"
#Fonction
screen = Tk()
def Python():
    webbrowser.open("https://docs.python.org/fr/3")
def C():
    webbrowser.open("https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-170")
def Cpp():
    webbrowser.open("https://docs.microsoft.com/fr-fr/cpp/cpp/?view=msvc-170")
def bash():
    webbrowser.open("https://www.gnu.org/software/bash/manual/bash.html")
def Htlm():
    webbrowser.open("https://www.w3schools.com/tags/tag_doctype.asp")
def Css():
    webbrowser.open("https://www.w3schools.com/Css/")
#Fenetre
screen.config(bg=Color)
screen.title("Arrera Documentation")
screen.minsize(800,150)
screen.maxsize(800,150)
screen.iconphoto(False,PhotoImage(file="image/Icon.png"))
#Cadre
cadreLanguage = Frame(screen,bg=Color,width=775,height=250)
#Bouton
BoutonPython = Button(cadreLanguage,text="Python",command=Python,bg=Color)
IconPython = PhotoImage(file="image/python.png",master=BoutonPython)
BoutonPython.image_names = IconPython
BoutonPython.config(image=IconPython)
BoutonC = Button(cadreLanguage, text="Language C",command=C,bg=Color)
IconC = PhotoImage(file="image/c.png",master=BoutonC)
BoutonC.image_names = IconC
BoutonC.config(image=IconC)
BoutonBash = Button(cadreLanguage,text="Bash",command = bash,bg=Color)
IconBash = PhotoImage(file="image/bash.png",master=BoutonBash)
BoutonBash.image_names = IconBash
BoutonBash.config(image=IconBash)
BoutonCpp = Button(cadreLanguage, text="LanguagebC++",command=Cpp,bg=Color)
IconCpp =PhotoImage(file="image/cpp.png",master=BoutonCpp)
BoutonCpp.image_names = IconCpp
BoutonCpp.config(image=IconCpp)
BoutonHtml = Button(cadreLanguage,text="HTML",bg=Color,command=Htlm)
IconHtlm = PhotoImage(file="image/htlm.png",master=BoutonHtml)
BoutonHtml.image_names = IconHtlm
BoutonHtml.config(image=IconHtlm)
BoutonCSS = Button(cadreLanguage,text="CSS",bg=Color,command=Css)
IconCSS = PhotoImage(file="image/css.png",master=BoutonCSS)
BoutonCSS.image_names = IconCSS
BoutonCSS.config(image=IconCSS)
#Affichage
cadreLanguage.place(relx=.5, rely=.5, anchor="center")
BoutonPython.place(x="1",y="65")
BoutonBash.place(x="718",y="65")
BoutonCpp.place(x="150",y="65")
BoutonC.place(x="568",y="65")
BoutonHtml.place(x="300",y="65")
BoutonCSS.place(x="418",y="65")
#Fin Programme
screen.mainloop()