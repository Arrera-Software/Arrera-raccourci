import webbrowser
import subprocess
from objet.ObjetJSON import *
from objet.detectionOS import *
import os

class CommandWeb :
    def __init__(self,nb : str):
        self.fichierJSON = jsonWork("racourcie/configBTN/btnDoc"+nb+".json")
    
    def open(self):
        lien = str(self.fichierJSON.lectureJSON("lien"))
        webbrowser.open(lien)
        
class CommandFile : 
    def __init__(self,nb : str) :
        os = OS()
        self.__linuxOS = os.osLinux()
        self.__windowsOS = os.osWindows()
        del os
        self.__fileJson = jsonWork("racourcie/configBTN/btnDoc"+nb+".json")

    
    def open(self):
        if ((self.__linuxOS == True) and (self.__windowsOS == False)):
            subprocess.run(['xdg-open', self.__fileJson.lectureJSON("lien")], check=True)
        elif ((self.__linuxOS == False) and (self.__windowsOS == True)):
            os.startfile(self.__fileJson.lectureJSON("lien"))