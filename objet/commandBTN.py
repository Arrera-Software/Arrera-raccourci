import webbrowser
import subprocess
import sys
from objet.ObjetJSON import *

class CommandWeb :
    def __init__(self,nb : str):
        self.fichierJSON = jsonWork("racourcie/configBTN/btnDoc"+nb+".json")
        print("racourcie/btnDoc"+nb+".json")
    
    def open(self):
        lien = str(self.fichierJSON.lectureJSON("lien"))
        webbrowser.open(lien)
        
class CommandFile : 
    def __init__(self,nb : str) :
        self.file = str("racourcie/fichier/doc"+nb+".pdf")
    
    def open(self):
        if sys.platform == "win32":
            # Sur Windows
            subprocess.Popen(["start", self.file], shell=True)
        elif sys.platform == "darwin":
            # Sur macOS
            subprocess.Popen(["open", self.file])
        else:
            # Sur Linux et autres systèmes Unix
            subprocess.Popen(["xdg-open", self.file])
    
   
        