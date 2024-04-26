#!/usr/bin/python3
"""Module doc"""

def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)

    for i in range (n):
        for j in range (i,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(n):
        temp = matrix[i][0]
        matrix[i][0] = matrix[i][n-1]
        matrix[i][n-1] = temp
