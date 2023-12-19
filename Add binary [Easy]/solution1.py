'''

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

def addBinary(a: str, b: str) -> str:
    
    # 直接相加,轉換成str:list
    sum = list(str(int(a) + int(b)))
    dsum = [int(x) for x in sum]

    # 進位
    n = len(dsum) - 1

    # 進位
    while n >= 0:
        if dsum[n] >= 2:
            if n != 0:
                dsum[n] %= 2
                dsum[n-1] = dsum[n-1] + 1
            else:
                dsum.insert(0,dsum[0]//2)
                dsum[1] %= 2
        n -= 1

    sum = [str(x) for x in dsum]
    return "".join(sum)

a = "1111"
b = "1111"

ans = addBinary(a,b)
print(ans)

