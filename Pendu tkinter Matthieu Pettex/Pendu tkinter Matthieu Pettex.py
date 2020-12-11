# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:22:14 2020

@author: matpe
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:07:50 2020

@author: matpe
"""

from random import choice
from tkinter import Tk, Label, StringVar, Entry, Button, Canvas, PhotoImage, messagebox

"""fonctions"""
def fMotAléatoire (): #fonction qui permet de lire un fichier texte, de séparer les mots et de les rangers dans une liste
    fich=open("mots test.txt","r")  
    contenu=fich.read()
    fich.close()
    contenu=contenu.replace('"','')
    contenu=contenu.replace('.','')
    contenu=contenu.replace('\n','') #cette suite de ligne permettrait de transformer presque n'importe quel texte en suite de mot, intégrables dans une liste !
    contenu=contenu.replace(',','')
    contenu=contenu.replace(';','')
    contenu=contenu.replace("'",'')
    listeMots=contenu.split()
    motA=choice(listeMots).upper()
    return motA #cette fonction return un mot prit dans la liste au hasard


def fVerif(mot, lettreSaisie, affichage, listeLettresSaisies,vie):
    
    
    if lettreSaisie not in listeLettresSaisies:
        listeLettresSaisies.append(lettreSaisie) #si la lettre n'a pas déjà été choisie, elle est ajoutée à la liste des lettres choisies
    
    if lettreSaisie not in mot:
        return affichage, listeLettresSaisies,vie-1 #si la lettre choisie n'est pas dans le mot, l'utilisateur perd une vie
    affichage = list(affichage)
    for i,lettre in enumerate(mot):
        if lettre == lettreSaisie:
            affichage[i] = lettreSaisie
    affichage = ''.join(affichage)    
    
    return  affichage, listeLettresSaisies, vie

def fTour():
    """Cette fonction s'occupe de chaque tour de jeu et est appellée par le
    bouton valider"""
    global Mot, Display, ListeLettreEntrée, Vie, Winstreak  
    
    LettresValides = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    NouvelleLettre = str(Saisie.get()).upper()  #Recupère la lettre entrée par l'utilisateur dans l'entry
    
    if Vie == 0 or Display == Mot:    #Bloque le programme si le joueur n'a plus de vie ou le mot est trouvé
        return
    
    if NouvelleLettre not in LettresValides: #envoie une alerte à l'utilisateur pour lui signaler que ce qu'il propose n'est pas valide (n'est pas inclus dans la liste des lettres)
        messagebox.showinfo("Erreur","Ce que vous proposez n'est pas valide !")
    if NouvelleLettre in ListeLettreEntrée: #envoie une alerte à l'utilisateur pour lui signaler que ce qu'il propose a déjà été proposé (est inclus dans la liste des lettres déjà proposées)
        messagebox.showwarning("Erreur","Veuillez changer de lettre \n Cette lettre a déjà été donnée auparavant !")
    if NouvelleLettre not in ListeLettreEntrée and NouvelleLettre in LettresValides: #si la proposition est une lettre et n'est pas incluse dans la liste des lettres déjà proposées, elle y est rajoutée
        if NouvelleLettre not in Mot: #l'utilisateur perd une vie si sa lettre n'est pas dans le mot
            Vie -= 1
            ListeLettreEntrée.append(NouvelleLettre)
        else:
            Display, ListeLettreEntrée,Vie = fVerif(Mot, NouvelleLettre, Display, ListeLettreEntrée,Vie)
                                                          
                                                          
    #on met à jour les afficheurs dans le tkinter à chaque tour
    TexteLettreListe.config(text = ListeLettreEntrée)   
    TexteMotADecouvrir.config(text = " ".join(Display))
    TexteNombreVie.config(text = ListeLettreEntrée)
    TexteWinstreak.config(text =str('Série de victoires : '+str(Winstreak)+'| Meilleur score :'+str(max(listeScore))))
    TexteNombreVie.config(text = str('Vie : '+str(Vie)))

    #on met à jour les images, si l'utilisateur a 8 vie, le bonhome possède tout ses membres, et il en perd au fur et à mesure que l'utilisateur perd des vies
    if Vie == 8:
        item = CanvasPhoto.create_image(150, 150, image =photo1)
    elif Vie == 7:
        item = CanvasPhoto.create_image(150, 150, image =photo2)
    
    elif Vie == 6:
        item = CanvasPhoto.create_image(150, 150, image =photo3)
    
    elif Vie == 5:
        item = CanvasPhoto.create_image(150, 150, image =photo4)
    
    elif Vie == 4:
        item = CanvasPhoto.create_image(150, 150, image =photo5)
    
    elif Vie == 3:
        item = CanvasPhoto.create_image(150, 150, image =photo6)
    
    elif Vie == 2:
        item = CanvasPhoto.create_image(150, 150, image =photo7)
    
    elif Vie == 1:
        item = CanvasPhoto.create_image(150, 150, image =photo8)
    
    elif Vie == 0:
        item = CanvasPhoto.create_image(150, 150, image =photo9) #si l'utilisateur, la photo "game over" s'affiche et sa série de victoire est remise à zéro
        TexteMotADecouvrir.config(text = " ".join(Mot))          #de plus, le mot qu'il n'a pas réussi à trouver s'affiche et une alerte apparait pour lui annoncer qu'il a perdu
        Winstreak = 0
        messagebox.showwarning("Pas de chance","Vous avez perdu !")
   
    if Display == Mot:
       messagebox.showinfo("Bien joué","Vous avez gagné") #si il gagne, une alerte lui annonce qu'il a gagné, on rajoute le nombre de vie(s) restant à la liste des scores et sa série de victoires augmente de 1.
       Winstreak += 1
       listeScore.append(Vie)
       
def fRejouer():
    #Cette fonction s'occupe d'initialiser et de réinitialiser le programme
    global Mot, Display, ListeLettreEntrée, Vie
    Mot =  fMotAléatoire() #Choisi le mot au hasard dans le fichier txt
    ListeLettreEntrée = []
    
    try:    #Permet de savoir si il faut initialiser le pendu ou si il faut juste reinitialiser
        Display
    except NameError:
        Display = "_"*len(Mot) #ici, il s'agit de reinitialiser
    else:
        Display = "_"*len(Mot) #ici, d'initialiser (1ère partie)
        Display,ListeLettreEntrée,Vie = fVerif(Mot, Mot[0], Display, ListeLettreEntrée, Vie)   
                                                  
        TexteLettreListe.config(text = ListeLettreEntrée)
        TexteMotADecouvrir.config(text = " ".join(Display))
        
    Vie = 8
    #Pour avoir la première lettre
    Display,ListeLettreEntrée,Vie = fVerif(Mot, Mot[0], Display, ListeLettreEntrée, Vie)  
                                                  


"""initialisation des valeurs de série de victoire et liste des scores"""
Winstreak=0
listeScore=[0]
fRejouer() 

"""création de l'interface graphique tkinter"""
FenetrePendu = Tk() #créé la fenêtre tkinter
boutonQuitter = Button(FenetrePendu, bg='pink', text = 'Quitter', fg = 'red', command = FenetrePendu.destroy)
boutonRejouer = Button(FenetrePendu, bg='lightgreen', text = 'Rejouer', fg = 'green', command = fRejouer)
boutonProposer = Button(FenetrePendu, bg='lightblue', text = 'Proposer', fg = 'blue', command = fTour) #on associe les fonctions vues précédemment avec ces boutons

      
#création des éléments 'Label' et 'Entry' appercevables dans tkinter:
TexteMotADecouvrir = Label(FenetrePendu, text =" ".join(Display))
TexteProposition = Label(FenetrePendu, text ='Proposez une lettre : ')
TexteLettre = Label(FenetrePendu, text ='Lettres déjà données :')
TexteLettreListe = Label(FenetrePendu, text = ListeLettreEntrée)
TexteWinstreak = Label(FenetrePendu, text =str('Série de victoires : '+str(Winstreak)+'| Meilleur score :'+str(max(listeScore))))
TexteNombreVie = Label(FenetrePendu, text = str('Vie : '+str(Vie)))
Saisie= StringVar()
BarreSaisie = Entry(FenetrePendu, textvariable = Saisie)


    
# création de l'élément 'Canvas'et importation des images du bonhomme:
CanvasPhoto = Canvas(FenetrePendu, width =300, height =300, bg ='white')
photo1 = PhotoImage(file ='Images/bonhomme1.gif')
photo2 = PhotoImage(file ='Images/bonhomme2.gif')
photo3 = PhotoImage(file ='Images/bonhomme3.gif')
photo4 = PhotoImage(file ='Images/bonhomme4.gif')
photo5 = PhotoImage(file ='Images/bonhomme5.gif')
photo6 = PhotoImage(file ='Images/bonhomme6.gif')
photo7 = PhotoImage(file ='Images/bonhomme7.gif')
photo8 = PhotoImage(file ='Images/bonhomme8.gif')
photo9 = PhotoImage(file ='Images/bonhomme9.gif')
  
item = CanvasPhoto.create_image(150, 150, image =photo1)
       
# Mise en page à l'aide de la méthode 'grid', j'aurais également pu utiliser les coordonnées x et y pour placer les éléments mais comme il y en a peu, il était plus simple d'utiliser grid.
TexteMotADecouvrir.grid(row =1, column =2)
TexteProposition.grid(row =2, column =1)
TexteLettre.grid(row =3, column =1) 
TexteLettreListe.grid(row =3, column =2)
TexteWinstreak.grid(row =4, column =2)
TexteNombreVie.grid(row =4, column =4)
BarreSaisie.grid(row =2, column =2,)
CanvasPhoto.grid(row =1, column =4, rowspan =3, padx =10, pady =5)

boutonQuitter.grid(row =5, column =2)
boutonProposer.grid(row =2, column =3)
boutonRejouer.grid(row =5, column =1)
  

FenetrePendu.title("Pendu | Matthieu Pettex | 3ETI | B")
FenetrePendu.mainloop()

#autocritique : j'aurais pu faire en sorte de vider le entry de a saisie à chaque tour et je n'ai pas réussi à faire continner le winstreak et le highscore comme je le souhaitais.
#vous pouvez m'envoyer un mail à matpettex@gmail.com si vous avez des remarques.