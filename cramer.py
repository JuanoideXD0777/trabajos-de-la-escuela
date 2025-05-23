def valores(matriz):
    det = determinante()
    x=dx()
    y=dx()
    z=dx()
    resultados=[]
    return resultados 

def determinante(matriz):
    return 48

def dx(matriz):
    return 0.5

def valores(matriz,independientes):
    resultados=[]
    det=dx()
    resultados.append(det)
    return resultados

def determinante(matriz):
    v1=0
    v2=0

#segun que esta funciona
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant