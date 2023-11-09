#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    unique_integers = set()
    total = 0
    for i in my_list:
        if isinstance(i, int):
            if i not in unique_integers:
                total += i
                unique_integers.add(i)

    return (total)
