import subprocess
import sys

class openPDF :
    def __init__(self,file):
        self.file = str(file)
    
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
        