from random import choice

"""même code que la version simplifiée mais avec plus de possibilités : trois langues différentes, 4 difficultés différentes
et le highscore et winstreak prennent en compte la difficulté, pas besoin de commentaires, c'est que des if"""

def motAléatoire ():
    n=1
    while n not in ('fr','ang','lat'):
        n=input("choisir la langue des mots du pendu (français : fr, anglais : ang, latin : lat):")
    if n == "fr":
        fich=open("mots fr.txt","r")
    if n == "ang":   
        fich=open("mots ang.txt","r")
    if n == "lat":    
        fich=open("mots lat.txt","r")

        
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

def nbVie ():
    diff=1
    while diff not in ("f","n","d","h"):
        diff=input("Choisir la difficulté de la partie de pendu (f=facile->13 vies n=normal->8 vies d=difficile->4 vies h=hardcore->1 vie) :")
    if diff=="f":
        return 13
    if diff=="n":
        return 8
    if diff=="d":
        return 4
    if diff=="h":
        return 1
def underscore(mot , lettresDS):
    motModifié = ''
    for i in mot:
        if i in lettresDS:
            motModifié=motModifié+ i + ' '
        else:
            motModifié=motModifié+ '_ '
            
    return motModifié[:-1]
        
    
def saisie():
    lettre = input('Entrez une lettre : ')
    listeLettreValide=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if len( lettre ) > 1 or lettre not in listeLettreValide:
        return saisie()
    else:
        return lettre.upper()
winStreakF=0
winStreakN=0
winStreakD=0
winStreakH=0
listeScoreF=[0]
listeScoreN=[0]
listeScoreD=[0]
rejouer=True
while rejouer:
    vie=nbVie()
    diff=vie
    if diff==13:
        partie="facile"
    if diff==8:
        partie="normal"
    if diff==4:
        partie="difficile"
    if diff==1:
        partie="hardcore"
    mot=motAléatoire()
    lettresDejaSaisies=[mot[0]]
    affichage=underscore(mot, lettresDejaSaisies)
    print( 'Mot à deviner : ' , affichage)
    
    while '_' in affichage and vie>0:
        lettre = saisie()
        if lettre in lettresDejaSaisies:
            print(lettre.upper()," a déjà été saisie.")
        else :
            if lettre not in lettresDejaSaisies:
                lettresDejaSaisies.append(lettre)
            if lettre not in mot:
                print(lettre.upper()," n'est pas dans le mot. Vous perdez donc une vie.")
                vie=vie-1
                    
            affichage = underscore(mot, lettresDejaSaisies)
            print( "\nMot à deviner : ", affichage , "\nNombre de vies restantes :",vie )
    if vie>0:
        print("Vous avez réussi à trouver le mot qui était : ",mot)
        
        if diff==13:
            listeScoreF.append(vie)
            winStreakF+=1
            print("Votre meilleur score en ",partie," sur cette session est :",max(listeScoreF))
            print("Vous êtes sur une série de ",winStreakF,"victoires en difficulté",partie,"!")
        if diff==8:
            listeScoreN.append(vie)
            winStreakN+=1
            print("Votre meilleur score en ",partie," sur cette session est :",max(listeScoreN))
            print("Vous êtes sur une série de ",winStreakN,"victoires en difficulté",partie,"!")
        if diff==4:
            listeScoreD.append(vie)
            winStreakD+=1
            print("Votre meilleur score en ",partie," sur cette session est :",max(listeScoreD))
            print("Vous êtes sur une série de ",winStreakD,"victoires en difficulté",partie,"!")
        if diff==1:
            winStreakH+=1
            print("Vous êtes sur une série de ",winStreakH,"victoires en difficulté",partie,"!")
    else:
        print("Vous n'avez pas réussi à trouver le mot qui était : ",mot)
        if diff==13:
            winStreakF=0
        if diff==8:
            winStreakN=0
        if diff==4:
            winStreakD=0
        if diff==1:
            winStreakH=0
        
                
    choix=int(input("Voulez vous rejouer ? (1=oui 0=non) :"))
    if choix==1:
        rejouer=True
    if choix==0:
        rejouer=False
        print("Au revoir !")






