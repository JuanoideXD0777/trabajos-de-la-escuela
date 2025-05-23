import math
import os
nm=int(input("cuantas mallas hay:"))
rp=[]
vol=[]
for i in range(nm):
    r=float(input(f"suma de resistencias de la malla {i+1} (ohms:)"))
    v=float(input(f"suma de voltajes en la malla {i+1} (V:)"))
    rp.append(r)
    vol.append(v)

rc=[(0)*nm for _ in range(nm)]

for i in range(nm):
    for j in range(i+1, nm):
        r=float(input(f"resistencia compartida entre malla {i+1} y malla {j+1} (0 si no hay):"))
        rc[i][j]=r
        rc[j][i]=r

for i in range(nm):
    ecuacion=f"{rp[i]}I{i+1}"

    for j in range(nm):
        if i!=j and rc [i][j] !=0:
            ecuacion +=f"+{rp[i][j]}I{j+1}"
    ecuacion+=f"={vol[i]}"
    print(f"ecuacion de malla{i+1}:{ecuacion}")