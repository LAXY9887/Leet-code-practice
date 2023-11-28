nums = [0,1,2,2,3,0,4,2]
val =2

idx = 0
k = 0
for i in range(len(nums)):
    if nums[idx] == val:
        nums.pop(idx)
        k += 1
        idx -=1
    idx += 1
    

print("ans nums:",nums)
print("ans k:",k)