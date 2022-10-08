"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):
    if len(items) == 0:
        print('{}')
    else:
        items = [str(i) for i in items]
        freq = dict(Counter(i for sub in items for i in (sub)))
        for key in (freq.keys()):
             print(key + ': ' + str(freq[key]))

    



