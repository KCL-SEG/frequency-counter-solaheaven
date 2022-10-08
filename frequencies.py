"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter
def frequencies(items):
    freq = dict(Counter(i for sub in items for i in set(sub)))
    for key in (freq.keys()):
         print(key + ': ' + str(freq[key]))



