from PIL import Image


class resizeIMG :
    def __init__(self,hauteur:int,largeur:int):
        self.hauteur = int(hauteur)
        self.largeur = int(largeur)
       
    def setImage(self,file:str):
        self.image = Image.open(file)
    
    def resize(self,nameNewImage:str):
        newImage = self.image.resize((50,50))
        newImage.save(nameNewImage+".png")
        
    def setImageAndResize(self,file:str,nameNewImage:str):
        self.image = Image.open(file)
        newImage = self.image.resize((50,50))
        newImage.save(nameNewImage+".png")