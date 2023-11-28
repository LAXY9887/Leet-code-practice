"""

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

def isPalindrome(x: int) -> bool:
    i = x
    n = 0
    while i >= 1:
        i = i/10
        n += 1

    a_sum = 0
    a_list = []
    for i in range(n):
        a = int((x%10**(i+1) - a_sum)/10**(i))
        a_list.append(a)
        a_sum += a

    ans_sum = 0
    for idx,each in enumerate(a_list):
        ans_sum += each * 10 ** (n-(idx+1))

    return ans_sum==x

ans = isPalindrome(-121)
print(ans)