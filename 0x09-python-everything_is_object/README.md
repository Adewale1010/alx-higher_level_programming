My solutions to Python - Everything is object tasks at ALX SE

0-answer.txt: Python function used to get the type of an object.

1-answer.txt: Python function to get the variable identifier (which is the memory address in the CPython implementation).

2. Right count

	In the following code, do a and b point to the same object? Answer with Yes or No.

		>>> a = 89
		>>> b = 100


3. Right count =

  In the following code, do a and b point to the same object? Answer with Yes or No.

    >>> a = 89
    >>> b = 89


4. Right count =

  In the following code, do a and b point to the same object? Answer with Yes or No.

    >>> a = 89
    >>> b = a


5. Right count =+

  In the following code, do a and b point to the same object? Answer with Yes or No.

    >>> a = 89
    >>> b = a + 1


6. Is equal

  What do these 3 lines print?

    >>> s1 = "Best School"
    >>> s2 = s1
    >>> print(s1 == s2)


7. Is the same

  What do these 3 lines print?

    >>> s1 = "Best"
    >>> s2 = s1
    >>> print(s1 is s2)


8. Is really equal

  What do these 3 lines print?

    >>> s1 = "Best School"
    >>> s2 = "Best School"
    >>> print(s1 == s2)


9. Is really the same

  What do these 3 lines print?

    >>> s1 = "Best School"
    >>> s2 = "Best School"
    >>> print(s1 is s2)


10. And with a list, is it equal

  What do these 3 lines print?

    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3] 
    >>> print(l1 == l2)


11. And with a list, is it the same

  What do these 3 lines print?

    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3] 
    >>> print(l1 is l2)


12. And with a list, is it really equal

  What do these 3 lines print?

    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 == l2)


13. And with a list, is it really the same

  What do these 3 lines print?

    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 is l2)


14. List append

  What does this script print?

    l1 = [1, 2, 3]
    l2 = l1
    l1.append(4)
    print(l2)


15. List add

  What does this script print?

    l1 = [1, 2, 3]
    l2 = l1
    l1 = l1 + [4]
    print(l2)


16. Integer incrementation

  What does this script print?

    def increment(n):
      n += 1

      a = 1
      increment(a)
      print(a)


17. List incrementation

  What does this script print?

    def increment(n):
      n.append(4)

      l = [1, 2, 3]
      increment(l)
      print(l)


18. List assignation

  What does this script print?

    def assign_value(n, v):
      n = v

      l1 = [1, 2, 3]
      l2 = [4, 5, 6]
      assign_value(l1, l2)
      print(l1)


19. Copy a list object

  Write a function def copy_list(l): that returns a copy of a list.

    The input list can contain any type of objects
    Your file should be maximum 3-line long (no documentation needed)


20. Tuple or not?

    a = ()
    Is a a tuple? Answer with Yes or No.
