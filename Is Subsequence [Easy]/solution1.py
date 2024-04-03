"""

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 

of the characters without disturbing the relative positions of the remaining characters. 

(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

"""

solution:

    1. Initiate pointer_s = 0 to track the correct sub sequence in s

    2. Loop through the t string, with each char as c, if c is equal to the first char of s, 
       update the pointer_s by adding 1, to check the next char in s.

    3. In the end, if pointer_s is equal to the length of s (All chars in s are checked), the s is sub sequnce of t.

    4. Specical cases, if s is empty, then return True

    5. Specical cases, if s only contains a single char, check if s is in t.

"""

s = "b"
t = "abc"

pointer_s = 0

is_subseq = False

if len(s) == 0: is_subseq = True
elif len(s) == 1: is_subseq =  s in t
else:
    for c in t:

        if c == s[pointer_s]:
            pointer_s += 1

        if pointer_s == len(s):
            is_subseq = True
            break

print(is_subseq)