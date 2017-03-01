from display import *
from draw import *
import math

print("Testing matrix functions...\n")

red_pill = new_matrix()
blue_pill = new_matrix()

add_point(red_pill, 1, 2, 3)
add_point(red_pill, 4, 5, 6)
add_point(red_pill, 7, 8, 9)
add_point(red_pill, 10, 11, 12)
add_point(red_pill, 13, 14, 15)

print("red_pill: \n")
print_matrix(red_pill)

print("blue_pill: \n")
print_matrix(blue_pill)

print("blue_pill -> Identity Matrix: \n")
ident(blue_pill)
print_matrix(blue_pill)

print("red_pill -> Scalar Multiplication: \n")
scalar_mult(red_pill, 2)
print_matrix(red_pill)

print("blue_pill * red_pill: \n")
matrix_mult(blue_pill, red_pill)
print_matrix(red_pill)
#red_pill should stay the same

'''
spoon = new_matrix(2,3)
boi = new_matrix(3,2)
spoon[0][0] = 1
spoon[0][1] = 4
spoon[1][0] = 2
spoon[1][1] = 5
spoon[2][0] = 3
spoon[2][1] = 6
boi[0][0] = 7
boi[0][1] = 9
boi[0][2] = 11
boi[1][0] = 8
boi[1][1] = 10
boi[1][2] = 12

print_matrix(spoon)
print_matrix(boi)
matrix_mult(spoon, boi)

^^ saw if generalized matrix multiplier worked
'''

spoon = [ [5,0,3,1], [2,6,8,8], [6,2,1,5], [1,0,4,6] ]
print("spoon: \n")
print_matrix(spoon)
boi = [ [7,1,9,5], [5,8,4,3], [8,2,3,7], [0,6,8,9] ]
print("boi: \n")
print_matrix(boi)
matrix_mult(spoon, boi)
print("spoon * boi:\n")
print_matrix(boi)
print("...Done testing matrix functions.\n")

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_edge(matrix, 250, 0, 0, 500, 250, 0)
add_edge(matrix, 500, 250, 0, 250, 500, 0)
add_edge(matrix, 250, 500, 0, 0, 250, 0)
add_edge(matrix, 0, 250, 0, 250, 0, 0)
print_matrix(matrix)

temp = new_matrix(len(matrix[0]), len(matrix))
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        temp[i][j] = matrix[i][j]
scalar_mult(temp, 1/math.sqrt(2))

print_matrix(temp)
translate_matrix=ident(new_matrix())
translate_matrix[3][0] = 100
print_matrix(translate_matrix)
matrix_mult(translate_matrix, temp)
print_matrix(temp)

'''
For some reason even though my matrix multiplier seemed to be working, I can't get any
other translations working :(
'''

matrix.extend(temp)
    
draw_lines( matrix, screen, color )
display(screen)
