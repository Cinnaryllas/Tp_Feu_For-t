import random, enum, copy

class Etat(enum.Enum):
     EnVie = 2
     EnFeu = 1
     EnCendre = 0

class Arbre():
    def __init__(self):
        self.__etat = Etat.EnVie

    def brule(self):
        if(self.__etat == Etat.EnVie):
            self.__etat = Etat.EnFeu

    def enCendre(self):
        if(self.__etat == Etat.EnVie):
            self.__etat = Etat.EnCendre

    def getEtat(self):
        return self.__etat

    def __str__(self):
        if(self.__etat == Etat.EnFeu):
            return "*"
        elif (self.__etat == Etat.EnCendre):
            return "#"

class Bouleau(Arbre):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        if(self.getEtat() == Etat.EnVie):
            return "B"
        else:
            Arbre().__str__()

    def propagation(self, foret, i, j):
        taille = len(foret)
        foret.enCendre()
        if(i>0 and j >0):
            foret[i-1][j-1].brule()
        if(i<taille-1 and j < taille):
            foret[i-1][j].brule()
        if(i<taille-1 and j < taille +1):
            foret[i-1][j+1].brule()
        if(i<taille and j < taille -1):
            foret[i][j-1].brule()
        if(i<taille and j < taille +1):
            foret[i][j+1].brule()
        if(i<taille+1 and j < taille -1):
            foret[i+1][j-1].brule()
        if(i<taille+1 and j < taille):
            foret[i+1][j].brule()
        if(i<taille+1 and j < taille +1):
            foret[i+1][j+1].brule()


class Chene(Arbre):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        if(self.getEtat() == Etat.EnVie):
            return "C"
        else:
            Arbre().__str__()

    def propagation(self, foret, i, j):
        taille = len(foret)
        foret.enCendre()
        if(i<taille-1):
            foret[i-1][j].brule()
        if(j < taille -1):
            foret[i][j-1].brule()
        if(j < taille +1 ):
            foret[i][j+1].brule()
        if(i<taille +1):
            foret[i+1][j].brule()
    
class Sapin(Arbre):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        if(self.getEtat() == Etat.EnVie):
            return "S"
        else:
            Arbre().__str__()
    
    def propagation(self, foret, i, j):
        taille = len(foret)
        foret.enCendre()
        if(i<taille-1):
            alea = random.randint(0,1)
            if(alea == 1):
                foret[i-1][j].brule()
        if(j < taille -1):
            alea = random.randint(0,1)
            if(alea == 1):
                foret[i][j-1].brule()
        if(j < taille +1):
            alea = random.randint(0,1)
            if(alea == 1):
                foret[i][j+1].brule()
        if(i<taille+1):
            alea = random.randint(0,1)
            if(alea == 1):
                foret[i+1][j].brule()

class Vide(Arbre):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return " "

    def propagation(self, foret, i, j):
        pass

class Foret():
    def __init__(self, pBouleau, pChene, pSapin, taille):
        self.arbres = []
        for i in range (0,taille):
            self.arbres.append([])
            for j in range (0,taille):
                alea = random.randint(0,100)
                if alea < pBouleau:
                    self.arbres[i].append(Bouleau())
                elif alea < pBouleau+pChene:
                    self.arbres[i].append(Chene())
                elif alea < pBouleau+pChene + pSapin:
                    self.arbres[i].append(Sapin())
                else:
                    self.arbres[i].append(Vide())

    def propage(self):
        copyForet = copy.deepcopy(self.arbres)
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                if(self.arbres[i][j].getEtat() == Etat.EnFeu):
                    self.arbres[i][j].propagation(copyForet, i, j)
        self.arbres = copyForet

    def miseAFeu(self, pos):
        self.arbres[pos][pos].brule()

    def encoreEnFeu(self):
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                if (self.arbres[i][j].getEtat()==Etat.EnFeu):
                    return True
        return False

    def afficheStats(self, step):
            count=0
            countB=0
            countC=0
            countS=0
            countV=0
            totalC=0
            totalS=0
            totalB=0
            totalV=0
            for i in range (0, len(self.arbres)):
                for j in range(0,len(self.arbres)):
                    if (isinstance(self.arbres[i][j],Chene)):
                        totalC+=1
                    if (isinstance(self.arbres[i][j],Bouleau)):
                        totalB+=1
                    if (isinstance(self.arbres[i][j],Sapin)):
                        totalS+=1
                    if (isinstance(self.arbres[i][j],Vide)):
                        totalV+=1

                    if (self.arbres[i][j].getEtat()==Etat.EnCendre):
                        count+=1
                        if (isinstance(self.arbres[i][j],Chene)):
                            countC+=1
                        if (isinstance(self.arbres[i][j],Bouleau)):
                            countB+=1
                        if (isinstance(self.arbres[i][j],Sapin)):
                            countS+=1
                        if (isinstance(self.arbres[i][j],Vide)):
                            countV+=1
            print ("Le pourcentage d'arbre cramé est: " + str(count*100/(len(self.arbres)**2)) +"%")
            print ("Le pourcentage de sapin cramé est: " + str(100*countS/totalS) +"%")
            print ("Le pourcentage de bouleau cramé est: " + str(100*countB/totalB) +"%")
            print ("Le pourcentage de chene cramé est: " + str(100*countC/totalC) +"%")
            print ("Le pourcentage d'herbe cramé est: " + str(100*countV/totalV) +"%")
            print ("La fôret à brulé en : " + str(step) +" étapes.")

    def __str__(self):
        res = "";
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                res += str(self.arbres[i][j]) + " "
            res += "\n"
        return res

class Simulation:

    def run():
        f = Foret(20,20,30,20)
        print(f)
        f.miseAFeu(5)
        step = 0
        while(f.encoreEnFeu()):
            print(f)
            f.propage()
            step +=1
        f.afficheStats(step)
Simulation.run()