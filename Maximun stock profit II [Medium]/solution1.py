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

price = [1,2,4,2,5,7,2,4,9,0,9]

p1 = 0
p2 = 1

current_profit = 0
next_profit = 0
profit = 0
hold = False

for i in range(len(price)-1):

    if price[p2] > price[p1]:
        current_profit = price[p2] - price[p1]
        hold = True
        
        if p2+1 <= len(price)-1:
            next_profit = price[p2+1] - price[p1]
        else:
            if hold:
                profit += current_profit
            
        if next_profit < current_profit and hold:
            profit += current_profit
            hold = False
            p1 = p2

    else:
        p1 = p2

    p2 += 1

print(profit)