def chercheEtudiant(noms, notes):
    a=input("voulez vous chercher un étudiant ?")
    if a == "non":
        print("ok bah déso")
    else:
        b=input("Quel étudiant voulez vous cherchez ?")
        for i in range(len(noms)):
            if noms[i] == b:
                print(noms[i]+" a eu comme note : "+ str(notes[i]))

def trierEtudiant(noms, notes): 
    sorted(notes, reverse=True)
    for i in range(len(noms)):
        print(str(i+1)+". "+noms[i]+" = "+str(notes[i]))

#fonction pour determiner quel eleve a la meilleur note
def meilleure_note(noms, notes):
    noteDeBase = 0
    nomDeBase="dude"
    for nom in noms:
        for note in notes:
            if note > noteDeBase:
                noteDeBase=note
                nomDeBase=nom
    print("La meilleur note est "+str(noteDeBase)+" de "+nomDeBase)

#fonction qui permet de determiner qui a eu plus de 10 et qui n'as pas eu plus de 10 et de l'afficher
def afficher_repartition(noms, notes):
    for i in range(len(noms)):
        if notes[i] >=10:
            print("L'élève "+noms[i]+" as eu plus de 10, son avenir est prometteur")
        else:
            print("L'élève "+noms[i]+" n'as pas eu plus de 10, son avenir est incertain")

#Permet de calculer la moyenne des notes de tout les eleves
def calculer_moyenne(notes):
    calculMoyenne=0
    for i in notes:
        calculMoyenne+=i
        calculMoyenneFinal=calculMoyenne/2
    print(calculMoyenneFinal)

#On demande a l'utilisateur le nombre d'élève a entrer
a=int(input("Combien d'élève voulez vous entrez ?"))
listeEtudiants=[]
listeNote=[]

#boucle qui permet de demander le nombre de fois qu'il a voulu le nom et la note de l'étudiant
for i in range(0,a):
    b=input("Comment s'appelle l'étudiant "+ str(i+1) +" ?")
    c=int(input("Quel est la note de l'étudiant ?"))
    listeEtudiants.append(b)
    listeNote.append(c)

#déroulement des résultat
print(listeEtudiants)
print(listeNote)
print("La moyenne des notes est :")
calculer_moyenne(listeNote)
afficher_repartition(listeEtudiants, listeNote)
meilleure_note(listeEtudiants, listeNote)
trierEtudiant(listeEtudiants, listeNote)
chercheEtudiant(listeEtudiants, listeNote)
