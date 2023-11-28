My solutions to Python - Test-driven development tasks at ALX SE

0. Integers addition

	0-add_integer.py: Python  function that adds returns the addition of two  integers.

	Prototype: def add_integer(a, b=98):
	a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
	a and b must be first casted to integers if they are float


1. Divide a matrix

	2-matrix_divided.py: Python function that divides all elements of a matrix and returns a new matrix

	Prototype: def matrix_divided(matrix, div):
	matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
	Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
	div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
	div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
	All elements of the matrix should be divided by div, rounded to 2 decimal places
