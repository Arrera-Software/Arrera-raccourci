from objetResize import *
from tkinter.filedialog import askopenfilename

icone = askopenfilename(defaultextension=".png", filetypes=[("Image", ".png")])
workIMG = resizeIMG(50,50)
nomImage = str(input("Entrer le nom de l'image : "))
workIMG.setImageAndResize(icone,nomImage)