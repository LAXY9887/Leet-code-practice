'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

"""
 f(X) = Xn + Xn-1
X = 1, 1
X = 2, 2
X = 3, 3
X = 4, 5
X = 5, 8
...
"""

def climbStairs(n: int) -> int:
    first = 1
    second = 2
    current = 0

    if n == 2: 
        return second
    elif n == 1:
        return first

    for i in range(n-2):
        current = first + second
        first = second
        second = current

    return current

print(climbStairs(2))

