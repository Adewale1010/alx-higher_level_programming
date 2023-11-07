#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for item in row:
            print(item, end="\t")
        print()
