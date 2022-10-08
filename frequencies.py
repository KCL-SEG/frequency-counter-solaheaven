"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from ast import main
from collections import Counter
def frequencies(items):
    freq = {}
    for i in items:
        freq[i] = items.count(i)
    return freq

dict = frequencies(items)
for key in (dict.keys()):
    print(key + ': ' + str(dict[key]))



