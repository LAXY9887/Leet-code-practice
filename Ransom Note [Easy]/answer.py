"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine 

and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

"""

solution:

    

"""

# Input
ransomNote = "aa"
magazine = "aab"

# Using the Counter to find the occurance of each different letter
from collections import Counter

note = Counter(ransomNote)
maga = Counter(magazine)

# They will become dictionary
print("note = ",note)
print("maga = ",maga)

# Intersect by the bitwise comparism " & "
Dict_intersect = note & maga
print("note & maga = ",Dict_intersect)

# If the intersect result is equal to note, the construction is avaliable
print(note == Dict_intersect)