import tkinter
import random
class Grille:
    def __init__(self, bateaux=[]):
        self.__bateaux = bateaux
        self.casesTestees = []
        self.casesTouchees = 0
    def valide(self):
        compte_bateaux = 0
        for bateau in self.__bateaux:
            compte_bateaux += 1
        return compte_bateaux == 5
    def ajouter_bateau(self, bateau):
        self.__bateaux += [bateau]
        return bateau
    def bateaux(self):
        return self.__bateaux
class Bateau:
    def __init__(self, coordonnees_origine = (0,0), direction=None, longueur=0):
        self.coordonnees= coordonnees_origine
        self.direction=direction
        self.longueur=longueur
        self.casestouchees=[]
        self.__cases_trouvees=0
        self.__coule=False
        cases=[self.coordonnees]
        for i in range (self.longueur-1):
            if self.direction == "bas":
                cases+=[(self.coordonnees[0],self.coordonnees[1]+(i+1))]
            if self.direction == "haut":
                cases+=[(self.coordonnees[0],self.coordonnees[1]-(i+1))]
            if self.direction == "droite":
                cases+=[(self.coordonnees[0]+(i+1),self.coordonnees[1])]
            if self.direction == "gauche":
                cases+=[(self.coordonnees[0]-(i+1),self.coordonnees[1])] 
        self.cases=cases
        __cases_trouvees=0
        # print(self.cases)
        # print(self.cases[0][0])
    def valide(self):
        valide=True
        for p in range (len(self.cases)):
            if self.cases[p][0]<= 8 and self.cases[p][0] >=1:
                valide=True
            else:
                return False
            if self.cases[p][1]<= 8 and self.cases[p][1] >=1:
                valide=True
            else:
                return False
        return(valide)
    def verifier(self) :# verifie si coordonnées du tk est = celle d un bateau
        case_bateau=self.cases
        return case_bateau
        # print(case_bateau)
    def cases_bateau(self): # renvoie la position des cases du bateau de type [(3,3),(4,3)]
        cases=[self.coordonnees]
        for i in range (self.longueur-1):
            if self.direction == "haut":
                cases+=[(self.coordonnees[0],self.coordonnees[1]+(i+1))]
            if self.direction == "bas":
                cases+=[(self.coordonnees[0],self.coordonnees[1]-(i+1))]
            if self.direction == "droite":
                cases+=[(self.coordonnees[0]+(i+1),self.coordonnees[1])]
            if self.direction == "gauche":
                cases+=[(self.coordonnees[0]-(i+1),self.coordonnees[1])]
        return cases
    def case_trouvee(self):
        self.__cases_trouvees+=1
        return self.__cases_trouvees
    def nb_cases_trouvees(self):
        return self.__cases_trouvees
cases_ordi_restantes = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
def appuyer(touche):
    # print (touche)
    # print(tester_case(grille_ordi,touche,True))
    grille_ordi.casesTestees+=[touche]
    if tester_case(grille_ordi,touche,True):
        grille_ordi.casesTouchees += 1
    case_ordi = (random.randint(1,8),random.randint(1,8))
    case_ordi_index = len(cases_ordi_restantes)-1
    case_ordi = cases_ordi_restantes.pop(random.randint(0,case_ordi_index))
    case_ordi_resultat = tester_case(grille_joueur, case_ordi)  # l'ordi joue contre le joueur de façon aléatoire
    if case_ordi_resultat:
        print("L'ordi a touché un bateau")
    else:
        print("L'ordi a raté")
def generer_bateau(l):
    directions = ['haut','bas','droite','gauche']
    d_b = directions[random.randint(0,len(directions)-1)]
    if d_b == "haut":
        o_b = (random.randint(1,8), random.randint(l+1,8))
    elif d_b == "bas":
        o_b = (random.randint(1,8), random.randint(1,9-l))
    elif d_b == "droite":
        o_b = (random.randint(1,9-l), random.randint(1,8))
    else:
        o_b = (random.randint(1+l,8), random.randint(1,8))
    return Bateau(o_b, d_b, l)
def tester_case(grille_test, coordonnees=(random.randint(1,8), random.randint(1,8)), joueur=False):
    partie_terminee=True
    b_trouves=0
    for b in grille_ordi.bateaux():
        if b.nb_cases_trouvees() == b.longueur:
            b_trouves += 1
        if b_trouves == 5:
            return
    for b in grille_test.bateaux():
        for case_test in b.cases:
            # print("CASE TEST :"+str(case_test)+"COORDONNEES :"+str(coordonnees))
            if case_test[0] == coordonnees[0] and case_test[1] == coordonnees[1]:
                if joueur:
                    p = tkinter.Label(gui,borderwidth=2, relief="groove",bg="#FF0000",fg="#000000",height=4, width=8)
                    p.grid(row=coordonnees[1],column=coordonnees[0])
                b.case_trouvee()
                #if b.cases
                return True
        if joueur:
            p = tkinter.Label(gui,borderwidth=2, relief="groove",bg="#FFFFFF",fg="#000000",height=4, width=8)
            p.grid(row=coordonnees[1],column=coordonnees[0])
    return False
    



cases_testees_ordi = []
grille_joueur = Grille()
longueurs_bateaux=[2,2,3,3,4]
bateau_joueur_initialisation = Bateau()
for i in range(5):
    x_orig=0
    y_orig=0
    direction=None
    print("Entrez les données du bateau "+str(i))
    while x_orig < 1 or x_orig > 8:
        x_orig=int(input("Entrez l'ordonnée du bateau (compris entre 1 et 8) :")) # x et y sont inversés
    while y_orig < 1 or y_orig > 8:
        y_orig=int(input("Entrez l'abscisse du bateau(compris entre 1 et 8) :"))
    while direction not in ["haut","bas","gauche","droite"]:
        direction = input("Entrez la direction du bateau( haut, bas, gauche, droite) :")
    bateau_joueur_initialisation.coordonnees = (x_orig, y_orig)
    bateau_joueur_initialisation.direction = direction
    bateau_joueur_initialisation.longueur = longueurs_bateaux[i]
    # print(bateau_joueur_initialisation.valide())
    # print(bateau_joueur_initialisation.cases_bateau())
    # print(bateau_joueur_initialisation.coordonnees,bateau_joueur_initialisation.direction,bateau_joueur_initialisation.longueur)
    grille_joueur.ajouter_bateau(bateau_joueur_initialisation)
    
    
grille_ordi = Grille()
grille_ordi.ajouter_bateau(generer_bateau(2))
grille_ordi.ajouter_bateau(generer_bateau(2))
grille_ordi.ajouter_bateau(generer_bateau(3))
grille_ordi.ajouter_bateau(generer_bateau(3))
grille_ordi.ajouter_bateau(generer_bateau(4))



gui=tkinter.Tk()
gui.configure(background="#BABBBA")
gui.title("Bataille Navale")
gui.geometry("650x650")




horizontal = ["O","A","B","C","D","E","F","G","H"]
colonne=0
for horizon in horizontal :
    h = tkinter.Label(gui, text=str(horizon),bg="#989898",fg="#000000",height=4, width=8)
    # h.grid(row=ligne,column=colonne)
    h.grid(row=0,column=colonne)
    colonne+=1
    
verticale =["0",1,2,3,4,5,6,7,8]
ligne=0
for vertical in verticale :
    h = tkinter.Label(gui, text=str(vertical),bg="#989898",fg="#000000",height=4, width=8)
    # h.grid(row=ligne,column=colonne)
    h.grid(row=ligne,column=0)
    ligne+=1
    
    
cases=[]   
ca=1
li=1
for i in range (0,64):
    if ca == 9 :
        ca=1
        li+=1
    cases.append((ca,li))
    ca+=1
    
c=1
l=1
for case_ in cases:
    p= tkinter.Label(gui,bg="#EAE4E4",borderwidth=2, relief="groove",height=4, width=8)
    p.bind("<Button-1>",lambda e, case_=case_: appuyer(case_))
    p.grid (row=l,column=c)
    c+=1
    if c==9: 
        c=1
        l+=1

gui.mainloop()