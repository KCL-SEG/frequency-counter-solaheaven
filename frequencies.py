"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):
    freq = dict(Counter(i for sub in items for i in set(sub)))
    

dict = frequencies(items)
for key in (dict.keys()):
    print(key + ': ' + str(dict[key]))



