import os
os.system("cls")

ls = [3,5,8,6,5,9,2,3,5]     #es la lista 

print(ls)                    #imprime la lista original

for i in range(len(ls)):                #primera iteracion de la busqueda
    for j in range(len(ls)-i-1):        #segunda iteracion de la busqueda
        if ls[j] > ls[j+1]:             #si el numero siguiente es menor que el anterior...
            cc=ls[j]                    #la variable cc es igual al numero actual
            ls[j]=ls[j+1]               #el numero siguiente estara en la posicion actual
            ls[j+1]=cc                  #el numero actual ahora esta en la posicion correcta
            print(ls)                   #se imprime el resultado