class Dico:

    def addToDictio(motFR, motEN, d):
        for cle, valeur in d.items():
            if (cle == motFR or valeur == motEN):
                print("Ce mot est déjà dans le dictionnaire")
                break
            
        d[motFR] = motEN

    def returnAllDico(self,d):
            return d
    
    def returnEnOnly(self,d):
        for cle in d.keys():
            print(d[cle])

    def delFromDico(self,char, d):

        delList = []

        char = char[0]
        for i in d:
            if (char == i[0]):
                delList.append(i)

        for i in delList:
            del d[i]

Dictionnaire = {"Mot":"Word", "Terre":"Earth", "Jeu":"Game", "Essayer":"Try", "Pousser":"Push", "Nul":"Bad"}  
Dico.addToDictio("Mot", "Word", Dictionnaire)   
Dico.addToDictio("Nettoyer", "Clean", Dictionnaire)
print(Dico().returnAllDico(Dictionnaire))
Dico().returnEnOnly(Dictionnaire)
Dico().delFromDico("Non",Dictionnaire)
print(Dico().returnAllDico(Dictionnaire))