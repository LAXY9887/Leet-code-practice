# Number list
nums = [3,3]

# Target number
target = 6

# Keep nums
initial_nums = nums.copy()

for i in range(len(nums)):

    # Track index
    idx1 = i

    # Choose an element for testing
    test = nums.pop(i)

    # Add it to the rest of the list
    tmpl = [each+test for each in nums]

    # Restore nums
    nums = initial_nums.copy()
    
    # Find target number index
    if target in tmpl:
        idx2 = tmpl.index(target) + 1
        break
    else:
        idx2 = -1

res = [idx1,idx2]

print(res)