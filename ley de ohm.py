import math
import os
os.system("cls")
def Voltaje():
    print("cual es la intensidad")
    intensidad=float(input())
    print("cual es la resistencia")
    resistencia=float(input())
    voltaje=intensidad*resistencia
    print("el voltaje es", (voltaje))

def Intensidad(voltaje,resistencia):
    intensidad=voltaje/resistencia
    print("la intensidad es",(intensidad))    

def Resistencia(intensidad,voltaje):
    return voltaje/intensidad

print("voltaje, intensidad o resistenca")
print("voltaje=1")
print("intensidad=2")
print("resistencia=3")
d=int(input(":"))
if d==1:
    Voltaje()
if d==2:
    voltaje=int(input("valor del voltaje:"))
    resistencia=int(input("valor de la resistencia:"))
    Intensidad(voltaje,resistencia)
if d==3:
    intensidad=int(input("intensidad de la corriente:"))
    voltaje=int(input("valor del voltaje:"))
    Resistencia(voltaje,intensidad)