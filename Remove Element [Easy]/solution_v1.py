
nums = [0,1,2,3,3,0,4,3]
val =3

def removeElement(nums: list[int], val: int) -> int:
    k = 0
    while val in nums:
        nums.remove(val)
        k += 1   
    print("ans:",nums)
    return k

print("ans:",removeElement(nums,val))