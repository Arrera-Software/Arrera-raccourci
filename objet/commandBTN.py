import webbrowser
from objet.openPDF import*
from objet.ObjetJSON import *

class CommandWeb :
    def __init__(self,nb : str):
        self.fichierJSON = jsonWork("racourcie/configBTN/btnDoc"+nb+".json")
    
    def open(self):
        lien = str(self.fichierJSON.lectureJSON("lien"))
        webbrowser.open(lien)
        
class CommandFile : 
    def __init__(self,nb : str) :
        self.pdf = openPDF("racourcie/fichier/doc"+nb+".pdf")
    
    def open(self):
       self.pdf.open()
    
   
        