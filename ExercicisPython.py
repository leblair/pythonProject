"""num1 = float(input("Entra un nombre:"))
num2 = float(input("Entra un segon nombre:"))

def average(num1,num2):
    print((num1+num2)/2)

print("La seva mitjana aritmetica es:")
average(num1,num2)"""
import math

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

"""set1 = {"hola","adios","noche","dia"}
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
    print(u)"""

"""int1 = int(input("Entra el primer nombre enter:"))
int2 = int(input("Entra el segon nombre enter:"))
def divExact(int1, int2):
    if(int2==0):
        print("No es pot dividir per 0")
    res = int1%int2
    if(res==0):
        print("Divisio exacta, residu:", res)
    else:
        print("Divisio no exacta, residu", res)

divExact(int1,int2)"""

"""def areaTC():
    option = int(input("Quina area vols calcular?\n1. Triangle\n2. Cercle\n"))
    if(option==1):
        base = float(input("Entra la base:"))
        height = float(input("Entra l'altura:"))
        print("L'area d'aquest triangle es: ", base*height/2)
    elif(option==2):
        radius = float(input("Entra el radi del cercle:"))
        print("L'area d'aquest cercle es: " , math.pi*pow(radius,2))
    else:
        print("No es una opcio valida")
areaTC()"""

def splitEuros():
    cant = int(input("Entra la quantitat d'euros:"))
    cont = 0
    fifty =0
    twenty =0
    ten =0
    five =0
    two =0
    one =0
    if(cant%50==0):
        fifty=cant/50
        print(fifty," Bitllets de 50€")
    elif(cant%20==0):
        twenty = cant/20
    elif(cant%10==0):
        ten = cant/10
    elif(cant%5==0):
        five = cant/5
    elif(cant%2==0):
        two = cant/2
    elif(cant%1==0):
        one = cant

    for i in range(1,cant):
        if(i==50):
            cont+=1
        elif(i==20):

