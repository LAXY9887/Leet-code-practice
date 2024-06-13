"""

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

## Solution, Two pass greedy method (Select local optimal solution)

    1. Initialize a candy_list [1,1,1,...] length = ratings. (Each person has 1 candy at the begining)

    2. First pass: Loop through the ratings list from index = 1, compare the score with left one, if current score
       
       is higher, add 1 to the corresponse position in candy_list.

    3. Second pass: Loop through the ratings list reversely, compare the score with right one, if current score
       
       is higher, add 1 to the corresponse position in candy_list.

    ¡° In 1st pass, add the candy number will be equal to the neighbor then add 1.
    ¡° In 2nd pass, the candy number will be the larger number between itself and neighbor + 1.

"""
# Rating list
ratings = [29,51,87,87,72,12]

# Initialize Candy list, which the length = ratings
n = len(ratings)
candy_list = [1] * n

for i in range(1,n,1):
    if ratings[i] > ratings[i-1]:
        candy_list[i] = candy_list[i-1] + 1

for i in range(n-2,-1,-1):
    if ratings[i] > ratings[i+1]:
        candy_list[i] = max(candy_list[i],candy_list[i+1]) + 1 

print(sum(candy_list))