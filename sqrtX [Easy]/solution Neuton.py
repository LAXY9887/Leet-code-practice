'''

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

'''

def mySqrt(x: int) -> int:
    pass

S = 25

precision = 1e-15

"牛頓法公式, 求 S 平方根, 1 < X < S: Xn+1 = 1/2*(Xn + S/Xn)"

def neuton(X):
    iter = 0.5*(X + S/X)
    while abs(iter**2 - S) > precision:
        return neuton(iter)
    return iter

X0 = 1
ans = neuton(X0)
print(ans)