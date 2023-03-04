"""
Problem - 1
Given two strings s1 and s2 check if they're anagrams. Two strings are anagrams if they're made of the same
frequencies.

input : s1 = danger and s2 = garden
output : true

Hint : Hash table
"""

"""
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in s1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in s2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True
"""

# Example 2

"""
from collections import Counter


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)
"""
"""
Two anagrams have the same lexicographically sorted string
input : s1 = nameless and  s2 = salesman
Sorted = ('nameless') = aeelmnss
Sorted = ('salesman') = aeelmnss

T(n)
"""
"""

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
"""
