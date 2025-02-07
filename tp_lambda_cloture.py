from functools import reduce

#Exercice 1
#question 1.1
def cardex(x):
    carreDeX = lambda x: x*x
    return carreDeX(x)

print(cardex(2))

#question 1.2
l=[1,2,3,4,5]
aucarre = map(lambda x: cardex(x),l)
print(list(aucarre))

#question 1.3
def sommeDeDeux(a, b):
    somme = lambda x,y:a+b
    return somme(a,b)

print(sommeDeDeux(3,4))

#question 1.4
sommedetout = reduce(lambda x,y: sommeDeDeux(x,y),l)
print(sommedetout)


#Exercice 2
#question 2.1
def mult(n):
    return lambda x:x*n

multi = mult(3)
print(multi(3))

#question 2.2
def double(n):
    dooble = mult(2)
    return dooble(n)

def triple(n):
    troople = mult(3)
    return troople(n)

#question 2.3
print(double(6)) 
print(triple(6)) 

#Exercice 3
#question 3.1
listeMot = ["eldenRing", "hollowKnight", "balatro", "webfishing", "tekken", "ark", "albionOnline"]

#question 3.2
filtre = filter(lambda x: "a" in x[0], listeMot)
print(list(filtre))

#question 3.3
def plusDeCinq():
    return lambda mot: len(mot)>5

f=plusDeCinq()
print()

filtre2 = filter(f ,listeMot)
print(list(filtre2))

#Exercice 5
def un():
    return lambda x :x+2

def deux():
    return lambda x : x*3

def compose(f, g):
    return lambda x : f(g(x))

trois = compose(un(),deux())
print(trois(5))
print(un()(3))

#Exercice 6
def unFilter(liste):
    return filter(lambda x: not " " in x, liste)

def unMap(liste):
    return map(lambda x : x.upper(), liste)

def filterMap(unFilter, unMap, uneListe):
    return unMap(unFilter(uneListe))

liste = ["a", "b", "c", "d", "e", " "]
print(list(filterMap(unFilter, unMap, liste)))


#Exercice 8
listeProduit = [["banane", "tekken8", "kiwi"],[10, 79, 0.50]]

def reduction(liste):
    return map(lambda x: x-(x*0.2), liste)

def calculateDiscount(reduction, list):
    return reduction(list)

print(list(calculateDiscount(reduction, listeProduit[1])))
