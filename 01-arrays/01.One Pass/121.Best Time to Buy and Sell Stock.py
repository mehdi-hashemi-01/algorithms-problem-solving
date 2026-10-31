#121. Best Time to Buy and Sell Stock

prices = [7,1,5,3,6,4]

max_profit = 0
min_price = prices[0]

for price in prices:
    if price < min_price:
        min_price = price

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit


print(max_profit)
print(min_price)





# for th in range(len(prices)):
#     for j in range(th+1,len(prices)):
#         profit = prices[j] - prices[th]
#         if profit > max_profit:
#             max_profit = profit
#
# print(max_profit)