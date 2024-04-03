"""

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 

However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

"""
"""

solution (Greedy algorism)

    1. This method optimize the local best solution, and hope for achieve the global optimiztion

    2. Although it often failed to be the best global solution, the outcome is somewhat useful.

    3. The method is simply sell the stock while it can make profit.

    4. Initialize time pointer p1 at 0 and p2 at 1, current profit = 0 and max profit (profit) = 0

    5. Loop through the price array and check the price of p2 is grater than p1, if so, buy and sell it,
       calculating current profit and add max profit by it.

    6. No matter the deal is made, update the time point p1 to p2. (Because we dont care about the global max profit)

    7. Update the p2 time point by 1.

    8. Max profit will be accumulated by local best deals.

"""


# Input
prices = [1,2,4,2,5,7,2,4,9,0,9]

# Time pointer
p1 = 0
p2 = 1

# Record profits
current_profit = 0
profit = 0

for i in range(len(prices)-1):

    # if prices at p2 > p1, buy and hold it, calculate current profit
    if prices[p2] > prices[p1]:
        current_profit = prices[p2] - prices[p1]

        # Add profit by current_profit
        # Update pointer p1 to p2
        profit += current_profit

    # Update p1 to p2 time point
    p1 = p2

    # Update p2 to next time point
    p2 += 1

print(profit)