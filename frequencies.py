"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):
    if len(items) == 0:
        return {}
    else:
        freq = {}
        items1 = list(map(str, items))
        for item in (items1):
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        return (freq)
    

   



