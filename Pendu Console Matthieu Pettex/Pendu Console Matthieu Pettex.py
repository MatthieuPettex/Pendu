# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:10:12 2020

@author: Matthieu Pettex
"""

from random import choice
from tkinter import Tk, Label, StringVar, Entry, Button, Canvas, PhotoImage


def fMotAléatoire ():#cette fonction lit un fichier texte, range les mots dans une liste et return un mot de cette liste au hasard
    fich=open("mots test.txt","r")  
    contenu=fich.read()
    fich.close()
    contenu=contenu.replace('"','')
    contenu=contenu.replace('.','')
    contenu=contenu.replace('\n','')
    contenu=contenu.replace(',','')
    contenu=contenu.replace(';','')
    contenu=contenu.replace("'",'')
    listeMots=contenu.split()
    motA=choice(listeMots).upper()
    return motA


def fUnderscore(mot , lettresDS):#cette fonction remplace les lettres du mot par des underscores "_" et remplace les underscores par les lettres proposées par l'utilisateur si celles-ci appartiennent au mot.
    motModifié = ''
    for i in mot:
        if i in lettresDS:
            motModifié=motModifié+ i + ' '
        else:
            motModifié=motModifié+ '_ '
            
    return motModifié[:-1]
        
    
def fSaisie():#cette fonction demande à l'utilisateur de rentrer une lettre et vérifie la validité de cette-ci
    lettre = input('Entrez une lettre : ')
    listeLettreValide=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if len( lettre ) > 1 or lettre not in listeLettreValide:
        return fSaisie()
    else:
        return lettre.upper()
#initialisatin des données
winStreak=0
listeScore=[0]
rejouer=True
while rejouer:
    vie=8
    mot=fMotAléatoire()
    lettresDejaSaisies=[mot[0]]
    affichage=fUnderscore(mot, lettresDejaSaisies)
    print( 'Mot à deviner : ' , affichage)
    
    while '_' in affichage and vie>0: #la partie continue tant que l'utilisateur a des vies et que le mot n'a pas été trouvé
        lettre = fSaisie()
        if lettre in lettresDejaSaisies:
            print(lettre.upper()," a déjà été saisie.") #vérifie si la lettre à déjà été proposée ou pas.
        else :
            if lettre not in lettresDejaSaisies:
                lettresDejaSaisies.append(lettre)
            if lettre not in mot:
                print(lettre.upper()," n'est pas dans le mot. Vous perdez donc une vie.")
                vie=vie-1 #si la lettre n'est pas dans le mot, l'utilisateur perd une vie
                    
            affichage = fUnderscore(mot, lettresDejaSaisies)
            print( "\nMot à deviner : ", affichage , "\nNombre de vies restantes :",vie )
    if vie>0: #si la partie se termine et que l'utilisateur a encore des vies, il gagne, sa série de victoires augmente de 1 et le nombre de vies restant est ajouté à la liste des scores
        print("Vous avez réussi à trouver le mot qui était : ",mot)
        listeScore.append(vie)
        winStreak+=1
        print("Vous êtes sur une série de ",winStreak,"victoires !")
        print("Votre meilleur score sur cette session est :",max(listeScore)) #le highscore correspond au max des scores dans la liste
    else:
        print("Vous n'avez pas réussi à trouver le mot qui était : ",mot) #si l'utilisateur n'a plus de vie, il perd, sa série de victoire est réinitialisée
        winStreak=0
        
                
    choix=int(input("Voulez vous rejouer ? (1=oui 0=non) :")) #demande à l'utilisateur si il souhaite relancer ou non
    if choix==1:
        rejouer=True
    if choix==0:
        rejouer=False
        print("Au revoir !")






