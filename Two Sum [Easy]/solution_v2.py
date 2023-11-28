nums = [15,4,2,3,8]

target = 18

hashmap = {}
for i in range(len(nums)):
    hashmap[nums[i]] = i


for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap and hashmap[complement] != i:
        print([i, hashmap[complement]]) 
        break