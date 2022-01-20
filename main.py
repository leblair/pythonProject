# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
list = ["a","b","c"]

for var in list:
    if(var=="b"):
        print(var)

"""squares = [x**2 for x in range[10]]
print(squares)"""

d = {"Nom": "Eva","Edat":3,"curs":"1"}
var = d["Nom"]
print(var)

"""dict.keys()"""

for x in d:
        print(x)

"""tupla es colleccion ordenada e inmutable permite duplicados"""

sorted = [2,4,11,-1]

sorted.sort()
sorted.reverse()
for i in sorted:
    print(i)



def metodo():
    print("Metodo1")
    def submetodo():
        met = "submetodo"
    submetodo()

metodo()
"""print(met," fuera de la clase")"""

