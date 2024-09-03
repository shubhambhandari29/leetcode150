'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Input: prices = [10,1,5,6,7,1]

Output: 6

'''





def maxProfit_mysol(prices):
    final_count=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]>=prices[j]:
                break
            else:
                count = prices[j]-prices[i]
                if final_count <count:
                    final_count =count
                continue
    return final_count

def max_profit(prices):
    # Initialize variables to track the minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0

    # Traverse through each price in the array
    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate the profit if selling at the current price
        profit = price - min_price
        # Update the maximum profit encountered so far
        if profit > max_profit:
            max_profit = profit

    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Output: 5

prices = [7, 6, 4, 3, 1]
print(max_profit(prices))  # Output: 0

        