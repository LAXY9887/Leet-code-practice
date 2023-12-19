'''

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''

def lengthOfLastWord(s: str) -> int:

    idx = len(s) - 1

    flag = False

    wc = 0

    while idx >= 0:
        
        if not flag and s[idx] != " ":
            flag = True

        if flag:
            if s[idx] != " ":
                wc += 1
            else:
                break

        idx -= 1

    return wc


s = "a"

ans = lengthOfLastWord(s)

print(ans)