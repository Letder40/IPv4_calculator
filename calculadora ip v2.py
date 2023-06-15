import os
import random
print("CALCULADORA IP                    ")
input("enter para continuar")
ips = []
seleccionador = []
def ip():
    global ips
    if ips != []:
        print(ips)
    bit = []
    numero = int(input("numero decimal   "))
    x=7
    for i in range(8):
        valor = pow(2,x)
        if numero >= valor:
            bit.append(1)
            numero = numero - valor
        else:
            bit.append(0)
        x = x - 1
    print(bit)
    ips.append(bit)
    input("enter para seguir")
    os.system("cls")
    ip()
def cip():
    bit = []
    valor2 = []
    x=0
    y=7
    for i in range(8):
        x = x+1
        bit.append(int(input("bit"+str(x)+"  ")))
    for i in range(8):
        potencia = pow(2,y)
        if bit[i]==1:
            valor2.append(potencia)  
        y=y-1
    valor_final = sum(valor2)
    print(valor_final)
    input("enter para seguir")
    os.system("cls")
    cip()
def aip():
    y = random.randint(1 , 255)
    x = random.randint(1 , 255)
    z = random.randint(1 , 255)
    h = random.randint(1 , 255)
    barra = random.randint(1 , 32)
    input("enter para generar ip")
    print (str(y) +"."+str(x)+"."+str(z)+"."+str(h)+"/"+str(barra))
    input("enter para continuar")
    os.system("cls")
    aip()
def menu():
    global seleccionador
    print("escribe ' 1 ' para seleccionar el modo decimal a binario")
    print("escribe ' 2 ' para seleccionar el modo binario a decimal")
    print("escribe ' 3 ' para seleccionar el modo ip aleatoria")
    seleccionador = input("selecciona el valor correspondiente   ")
    if seleccionador==str(1):
        ip()
    if seleccionador==str(2):
        cip()
    if seleccionador==str(3):
        aip()          
menu()


