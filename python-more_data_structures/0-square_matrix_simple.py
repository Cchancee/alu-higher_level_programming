#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k = []
    
    for row in range(len(matrix)):
        d = [i*i for i in matrix[row]]
        k.append(d)
    return k

'''
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print(square_matrix_simple(matrix))
'''
