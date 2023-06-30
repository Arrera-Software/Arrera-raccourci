import json

"""
file : Correspont a l'emplacement du fichier JSON
Flag : Correspont a quelle est l'emplacement de la valeur que vous voulez modifier ou lire
valeur :  correspont a la valeur que vous voulez modifer
vardict : Correspont au nom du dictionnaire que vous voulez rajouter
newDictName : corespont au dictionnaire que vous voulez rajouter   
"""
class jsonWork : 
    def __init__(self,file):
        self.fichier = file
        
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)
    
    def lectureJSONDict(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction et de le retourner sous forme de dictionnaire
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return dict
    
    def lectureSimpleJSON(self):#Permet de juste recuperer le contenu d'un fichier JSON
        with open(self.fichier, 'r') as openfile:
            dict = json.load(openfile)
        return dict
    
    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        openfile = open(self.fichier, 'r' , encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        writeFile = open(self.fichier, 'w', encoding='utf-8')
        dict[flag] = valeur
        json.dump(dict,writeFile,indent=2)
        
        
    def EcritureSansEcrasement(self,vardict,newDictName):#Permet d'ecrire un nouveau dictionnaire dans le fichier
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict1 = json.load(openfile)
        with open(self.fichier,"w", encoding='utf-8') as file :
            newdict = {newDictName : vardict} 
            alldict = dict(dict1,**newdict)
            json.dump(alldict,file,indent=2)
            
    def EcritureEcrasement(self,dictionnaire):#Permet d'ecrire dans un json en efacent son contenue
        with open(self.fichier, "w", encoding='utf-8') as f:
            json.dump(dictionnaire, f,indent=2)
            
    def compteurJSON(self):#Permet de compter le nombre de valeur dans un dictionnaire
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict1 = json.load(openfile)
            return len(dict1)