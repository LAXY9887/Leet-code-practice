# sorted list 1
num1 = [1,2,3,0,0,0]
m = 3

# sorted list 2
num2 = [2,5,6]
n = 3

# Fill up 0 to list2
myNum2 = [0]*m + num2

# Add up list1 and new_list2
newNum = [ x+y for x,y in zip(num1,myNum2)]

# Keep poping out min value to res list
res = []
for i in range(m+n):
    idx_min_n = newNum.index(min(newNum))
    res.append(newNum.pop(idx_min_n))

# sortted
num1 = res

# Print out result
print(num1)