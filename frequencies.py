"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):
    if len(items) == 0:
        return {}
    else:
        freq = {}
        for item in str(items):
            if (item in freq):
                freq[item] += 1
            if (type(item) is int) and item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return (freq)
    

   



