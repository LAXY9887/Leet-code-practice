"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Input: s = "{([])}"
Output: false

"""

def isValid(s: str) -> bool:

    brac_dict = {
        "(":")",
        "[":"]",
        "{":"}"
    }

    list_s = list(s)

    def ValidOne(ls:list) -> list:
        for i in range(len(ls)):

            current_s = ls[i]

            if i-1 >= 0 :
                prev_s = ls[i-1]
            else:
                prev_s = ""

            if (current_s not in brac_dict):
                if (prev_s in brac_dict) and (current_s == brac_dict[prev_s]):
                    ls.pop(i-1)
                    ls.pop(i-1)
                    break
        return ls
    
    while len(list_s) > 0:
        prev_list_s = list_s.copy()
        list_s = ValidOne(list_s)

        if prev_list_s == list_s:
            break

    return len(list_s) == 0


print(isValid("(){}}{"))
print(isValid("()[]{}"))
print(isValid("()"))
print(isValid("(]"))
print(isValid(")]"))
print(isValid("([)]"))
print(isValid("}"))
print(isValid("{()}"))
