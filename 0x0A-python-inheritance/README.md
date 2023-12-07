My Solutions to Python - Inheritance tasks at ALX SE


0. Lookup
	0-lookup.py: Python function that returns the list of available attributes and methods of an object.


1. My list
	1-my_list.py: Python class MyList that inherits from list.


2. Exact same object
	2-is_same_class.py: Python function that returns True if the object is exactly an instance of the specified class ; otherwise False.


3. Same class or inherit from
	3-is_kind_of_class.py: Python function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.


4. Only sub class of
	4-inherits_from.py: Python function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.


5. Geometry module
	5-base_geometry.py: Python empty class BaseGeometry.


6. Improve Geometry
	6-base_geometry.py: Python class BaseGeometry (based on 5-base_geometry.py).
		
		Public instance method: def area(self): that raises an Exception with the message area() is not implemented

7. Integer validator
	7-base_geometry.py: Python class BaseGeometry (based on 6-base_geometry.py).

		Public instance method: def area(self): that raises an Exception with the message area() is not implemented
		Public instance method: def integer_validator(self, name, value): that validates value:
			you can assume name is always a string
			if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
			if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0.


8. Rectangle
	8-rectangle.py: Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

		Instantiation with width and height: def __init__(self, width, height):
			width and height must be private. No getter or setter
			width and height must be positive integers, validated by integer_validator


9. Full rectangle
	9-rectangle.py: Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

		Instantiation with width and height: def __init__(self, width, height)::
			width and height must be private. No getter or setter
			width and height must be positive integers validated by integer_validator
		the area() method must be implemented
		print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>.


10. Square #1
	10-square.py: Python class Square that inherits from Rectangle (9-rectangle.py):

		Instantiation with size: def __init__(self, size)::
			size must be private. No getter or setter
			size must be a positive integer, validated by integer_validator
		the area() method must be implemented.


11. Square #2
	11-square.py: Python class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

		Instantiation with size: def __init__(self, size)::
			size must be private. No getter or setter
			size must be a positive integer, validated by integer_validator
		the area() method must be implemented
		print() should print, and str() should return, the square description: [Square] <width>/<height>.


12. My integer
	100-my_int.py: Python class MyInt that inherits from int.
		MyInt is a rebel. MyInt has == and != operators inverted

