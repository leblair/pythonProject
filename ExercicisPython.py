"""num1 = float(input("Entra un nombre:"))
num2 = float(input("Entra un segon nombre:"))

def average(num1,num2):
    print((num1+num2)/2)

print("La seva mitjana aritmetica es:")
average(num1,num2)"""

"""peus = float(input("Entra la primera distancia en peus:"))
polzades = float(input("Entra la distancia en polzades:"))

def distancia(peus,polzades):
    print("La primera distancia en cm es: ",peus*2.54*12)
    print("La segona distancia en cm es: ", polzades*2.54)

distancia(peus,polzades)"""

"""cel = float(input("Entra la temperatura en Celsius: "))

def celToFar(cel):
    print("La temperatura en Fahrenheit",1.8*cel+32)

celToFar(cel)"""

"""sec = float(input("Entra la quantitat de segons: "))

def castToMin(sec):
    min =int( sec/60)
    sleft = int(sec%60)
    print("Son ", min," minuts i ", sleft," segons")

castToMin(sec)"""

"""listaVocals = ["a","e","i","o","u"]

modificar = int(input("Quin numero de la llista vold modificar? "))
valor = input("Amb quin valor?")

def modList(lista,mod,valor):
    lista[mod] = valor
    for i in lista:
        print(i)
modList(listaVocals,modificar,valor)

lletra = input("Quina lletra de la llista vols modificar?")
valor = input("Amb quin valor?")
def modLet(lista,lletra,val):
    lista[lista.index(lletra)] = valor
    for i in lista:
        print(i)
modLet(listaVocals,lletra,valor)"""

"""multiples = [0,1,2,3,4,5,6,7,8,9,10]
listR = [x*7 for x in multiples]
for y in multiples:
    print("7 x ",y, " = ", listR[y])

map = {"Montse":0,"Bryan":10,"Oihane":5,"Raul":3}

alumne  = input("De quin alumne vols saber la nota? ")

print("La seva nota es: ",map[alumne])"""

set1 = {"hola","adios","noche","dia"}
set2 = {"good","bad","average","bland","noche"}
inter = set1.intersection(set2)
for s in inter:
    print(s)
print()
dif1 = set1.difference(set2)
for t in dif1:
    print(t)
print()
dif2 = set2.difference(set1)
for l in dif2:
    print(l)
print()
uni = set1.union(set2)
for u in uni:
    print(u)

