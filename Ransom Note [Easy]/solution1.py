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

    1. Turn the magazine into list() for using the remove() function

    2. Initialize a empty string reconstruct.

    3. Loop through the ransomNote with each letter c, check whether c is in magazine.

    4. if c is in magazine, Add c into reconstruct and remove it from magazine.

    5. In the end, compare the magazine to reconstruct to see whether they're the same.

"""

# Input
ransomNote = "aac"
magazine = "aab"


magazine = list(magazine)
reconstruct = ""

for c in ransomNote:

    if c in magazine:
        reconstruct += c
        magazine.remove(c)

print(reconstruct == ransomNote)