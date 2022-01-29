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

"""def printEuros(num,cant):
    if(num>=5):
        print("Billetes de ",num,"€: ", cant)
    else:
        print("Monedas de ",num,"€: ", cant)
def splitEuros():
    cant = int(input("Entra la quantitat d'euros:"))
    fifty =0
    twenty =0
    ten = 0
    five =0
    two =0
    one =1
    while cant>0:
        if(cant>=50):
            fifty = int(cant/50)
            cant = cant- fifty*50
            printEuros(50, fifty)
        elif(cant>=20):
            twenty = int(cant/20)
            cant = cant- twenty*20
            printEuros(20, twenty)
        elif(cant>=10):
            ten = int(cant/10)
            cant = cant- ten*10
            printEuros(10, ten)
        elif(cant>=5):
            five = int(cant/5)
            cant = cant- five*5
            printEuros(5, five)
        elif(cant>=2):
            two = int(cant/2)
            cant = cant- two*2
            printEuros(2, two)
        else:
            cant = cant-one
            printEuros(1, one)

splitEuros()"""

"""isValid = False
while(not isValid):
    day = int(input("Entra el dia: "))

    if(day<1 or day>31):
        print("No es un dia valid, entra un dia valid:")
    else:
        mes = int(input("Entra el mes: "))
        if mes<1 or mes >12 or (mes == 2 and day > 29) or ((mes == 4 or mes == 6 or mes == 9 or mes  ==11) and (day>30)) :
            print("No es un mes valid, entra un mes valid")
        else:
            any = int(input("Entra el any: "))
            if not(any%400==0 or (any%4==0 and any%100!=0)) and mes==2 and day>28:
                print("No es una data valida, entra una data valida:")
            else:
                print(day, "-", mes, "-", any)
                isValid = True"""
"""
def function13():

    valid = False
    varSum =0
    while not valid:
        nombre1 = int(input("Entra un nombre enter:"))
        nombre2 = int(input("Entra un segon nombre enter:"))
        if(nombre2<nombre1):
            print("El segon nombre es més gran que el primer, entra un altre nombre")
        else:
            for i in range(nombre1,nombre2+1):
                varSum +=i
            print("La suma dels seus nombres es: ",varSum)
            valid = True
function13()"""

def function14():
    valid = False
    listFac = []
    varFac =0
    while not valid:
        nFac = int(input("Entra un numero enter major que 0:"))
        if nFac<=0:
            print("No es un numero valid:")
        else:
            for a in range(1,nFac+1):
                listFac.append(a)

            for i in listFac:
                if i==2:
                    varFac +=(varFac+1)*i
                else:
                    varFac =varFac*i

            print("El factorial de ",nFac, " es ", varFac)
            valid = True

function14()