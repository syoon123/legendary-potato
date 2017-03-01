import math


def print_matrix( matrix ):
    pStr = ""
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            pStr += (str)(matrix[i][j]) + "\t"
        pStr += "\n"
    print(pStr)

def ident( matrix ):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x == y:
                matrix[y][x] = 1
            else:
                matrix[y][x] = 0
    return matrix
                

def scalar_mult( matrix, s ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = (int)(matrix[i][j]*s)
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    retMatrix = new_matrix(len(m1[0]), len(m2))    
    def dotrc( row, col ):
        s = 0
        for i in range(len(row)):
            s += (int)(row[i] * col[i])
        return s
    def getrow(j):
        arr = []
        for i in range(len(m1)):
            arr.append(m1[i][j])
        return arr
    for c in range(len(m2)):
        for r in range(len(m1[0])):
            row = getrow(r)
            col = m2[c]
            x = dotrc(row, col)
            retMatrix[c][r] = x
    #print retMatrix <== saw if generalized matrix multiplier worked
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            m2[i][j] = retMatrix[i][j]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
