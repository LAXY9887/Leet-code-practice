"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""

"""

solution:

    1. Create 2 pointer, p1 and p2, p2 is ahead of p1, initially p1 = 0, p2 = 1

    2. Create p to record current profit; profit as max profit

    3. Loop through the price array, if the p2 price is grater than p1, calculate current profit p

    4. if current profit p is grater than max profit, subsitute max profit to current profit p.

    5. Update p2 each step, if the p2 price is less than p1, change the p1 to p2, for calculating the section afterward.

"""

prices = [1,2,4,2,5,7,2,4,9,0,9]

p1 = 0
p2 = 1

p = 0
profit = 0

for i in range(len(prices)-1):

    if prices[p2] > prices[p1]:
        p = prices[p2] - prices[p1]
    else:
        p1 = p2

    if p > profit:
        profit = p

    p2 += 1

print(profit)