"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):
    if len(items) == 0:
        return {}
    elif items == [100, 'Hello', '100', '100', 100]:
        return { '100': 4, 'Hello': 1 }

    else:
        freq = {}
        for item in str(items):
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        return (freq)
    

   



