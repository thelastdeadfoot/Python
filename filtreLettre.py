from functools import reduce

#Exercice 1
l=[50, 20, 35, 100, 80]
conversion=map(lambda x: x*1.10, l)
print(list(conversion))

#Exercice2
age=[12, 25, 17, 18, 40, 15, 22]
extraireAge=filter(lambda x: x>=18, age)
print(list(extraireAge))

#Exercice3
listeVente=[120, 50, 30, 20, 90, 100]
total=reduce(lambda x,y: x+y, listeVente)
print("prix total : "+str(total))

#Exercice4
listeNote=[12, 15, 9, 18, 6, 20, 14]
conversionPonderer = list(map(lambda x: x * 5, listeNote))
extraireSup = list(filter(lambda x: x >= 50, conversionPonderer))
moyenTot=reduce(lambda x,y: x+y,extraireSup)
moyenTot2=moyenTot/len(extraireSup)
print(len(extraireSup))
print(list(conversionPonderer))
print(list(extraireSup))
print(moyenTot2)
