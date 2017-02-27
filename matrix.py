import math


def print_matrix( matrix ):
    pStr = ""
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            pStr += (str) (matrix[c][r]) + "\t"
        pStr += "\n"
    print(pStr)

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
