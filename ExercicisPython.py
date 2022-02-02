#Bryan Amaguana 2WIAM M10

def function1():
    num1 = float(input("Entra un nombre:"))
    num2 = float(input("Entra un segon nombre:"))
    print((num1 + num2) / 2)
    print("La seva mitjana aritmetica es:")
function1()
import math

def function2():

    peus = float(input("Entra la primera distancia en peus:"))
    polzades = float(input("Entra la distancia en polzades:"))

    print("La primera distancia en cm es: ",peus*2.54*12)
    print("La segona distancia en cm es: ", polzades*2.54)
function2()

def function3():
    cel = float(input("Entra la temperatura en Celsius: "))
    print("La temperatura en Fahrenheit",1.8*cel+32)

function3()

def function4():

    sec = float(input("Entra la quantitat de segons: "))
    min =int( sec/60)
    sleft = int(sec%60)
    print("Son ", min," minuts i ", sleft," segons")

def function5():
    listaVocals = ["a","e","i","o","u"]

    modificar = int(input("Quin numero de la llista vold modificar? "))
    valor = input("Amb quin valor?")

    listaVocals[modificar] = valor
    for i in listaVocals:
        print(i)

    lletra = input("Quina lletra de la llista vols modificar?")
    valor2 = input("Amb quin valor?")
    listaVocals[listaVocals.index(lletra)] = valor2
    for i in listaVocals:
        print(i)
function5()

def function6():

    multiples = [0,1,2,3,4,5,6,7,8,9,10]
    listR = [x*7 for x in multiples]
    for y in multiples:
        print("7 x ",y, " = ", listR[y])
function6()

def function7():

    map = {"Montse":0,"Bryan":10,"Oihane":5,"Raul":3}

    alumne  = input("De quin alumne vols saber la nota? ")

    print("La seva nota es: ",map[alumne])
function7()

def function8():
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
function8()

def function9():
    int1 = int(input("Entra el primer nombre enter:"))
    int2 = int(input("Entra el segon nombre enter:"))
    if(int2==0):
        print("No es pot dividir per 0")
    res = int1%int2
    if(res==0):
        print("Divisio exacta, residu:", res)
    else:
        print("Divisio no exacta, residu", res)

function9()

def function10():
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
function10()

def function11():

    def printEuros(num,cant):
        if(num>=5):
            print("Billetes de ",num,"€: ", cant)
        else:
            print("Monedas de ",num,"€: ", cant)

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

function11()

def function12():

    isValid = False
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
                    isValid = True


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
function13()

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

def function15():
    print("Multiples de 7 entre 0 i 100")
    for i in range(0,100,7):
        print(i)

function15()

def function16():
    num = int(input("Quantes paraules vols?:"))
    list = []
    for i in range(1,num+1):
        word = input("Escriu una paraula:")
        list.append(word)

    print(list)
function16()

def function17():
    numllista1 = int(input("Llista 1\nQuantes paraules vols?:"))
    list = []
    for i in range(1, numllista1 + 1):
        word = input("Escriu una paraula:")
        list.append(word)
    numllista2 = int(input("Llista 2\nQuantes paraules vols?:"))
    list2 = []
    for i in range(1, numllista2 + 1):
        word = input("Escriu una paraula:")
        list2.append(word)
    for i in list:
        if i in list2: list.remove(i)

    print("Lista 1 sin palabras de lista 2:\n",list)
function17()


def function18():
    num = int(input("Entra un numero:"))
    for i in range(2, num):
        if num % i == 0: return print(num, " no es un numero primer")
    return print(num, " es un numero primer")


function18()

def function19():
    print("Els numeros narcisistes fins el 1000 son:")
    for i in range(153,1000):
        x = int(i/100)
        y = int((i/10) % 10)
        z = i % 10
        if i == (x * x * x + y * y * y + z * z * z):
            print( i)

function19()

def function20():
    bool = False
    while not bool:
        n1 = int(input("Entra el primer nombre:"))
        n2 = int(input("Entra el segon nombre:"))
        if n1>n2 : print("El primer nombre es mes gran que el primer, entra un valor menor")
        else:
            for i in range(n1,n2+1):
                print(i)
            bool = True
function20()



def function21():
    bool = False
    while not bool:
        n1 = int(input("Entra el primer nombre:"))
        n2 = int(input("Entra el segon nombre:"))
        if n1 > n2:
            print("El primer nombre es mes gran que el primer, entra un valor menor")
        else:
            for i in range(n2, n1-1, -1):
                print(i)
            bool = True
function21()
import math

def function22():
    bool = False
    while not bool:
        n1 = int(input("Entra el primer nombre:"))
        n2 = int(input("Entra el segon nombre:"))
        if n1 > n2:
            print("El primer nombre es mes gran que el primer, entra un valor menor")
        else:
            print("Arrels quadrades entre ", n1, " i", n2)
            for i in range(n1,n2+1):
                print("Arrel quadrada de ",i ," = " ,math.sqrt(i))
            bool = True
function22()

def function23():
    bool = False
    while not bool:
        n1 = int(input("Entra el primer nombre:"))
        n2 = int(input("Entra el segon nombre:"))
        if n1 > n2:
            print("El primer nombre es mes gran que el primer, entra un valor menor")
        else:
            print("Nombres parells entre ", n1, " i", n2)
            for i in range(n1, n2 +1):
                if i%2 ==0: print(i)
            bool = True

function23()

#Bucles  i comprehension
def function24():
    listMult2 = [num*2 for num in range(1,11)]
    print("Els 10 primers multiples de 2 son: ",listMult2)
function24()

def function25():
    n = int(input("Entra quants multiples vols:"))
    m = int(input("De quin numero?:"))
    listMult = [num*m for num in range(1,n+1)]
    print("Els ", n, " primers multiples de ", m, " son", listMult)
function25()

def function26():
        word = input("Escriu una paraula:").lower()
        array = list(word)
        array.sort()
        newWord =""
        newWord = newWord.join(array)
        if newWord==word: print(word, " es una paraula alfabetica")
        else: print(word, " no es una paraula alfabetica")
function26()

def function27():
    chain = input("Escriu una cadena:").lower()
    array = chain.split(' ')
    arrayString =""
    arrayString = arrayString.join(array)
    list1 = list(arrayString)
    array2 = chain.split(' ')
    arrayString2 = ""
    arrayString2 = arrayString2.join(array2)
    list2 = list(arrayString2)
    list2.reverse()
    if list1 == list2: print(chain,"\nEs una cadena palindroma")
    else: print(chain, "\nNo es una cadena palindroma")
function27()


def function28():
    dic = dict.fromkeys(["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B","N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"])
    cont = 0
    boolean = False
    dni = ""
    for i in dic:
        dic.update({i: cont})
        cont += 1
    while not boolean:
        dni = input("Entra un DNI:")
        if len(dni) != 9: print("DNI no valido")
        else: boolean = True
    numDni = int(dni[0:-1])
    letra = dni[-1]
    if numDni % 23 == dic.get(letra): print("Lletra del DNI correcte")
    else: print("Lletra incorrecte")


function28()

def function29():
    file = open("functionFile.txt", "r")
    line = file.read().lower().split()
    print("Contingut del fitxer:\n", line)
    line = list(dict.fromkeys(line))
    line.sort()
    print("Paraules del fitxer ordenades sense repetits:\n",line)

function29()
