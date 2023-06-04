input_price = input('Enter numbers for the list separated by space: ')
print("\n")
prices = input_price.split()
# print list
print('list: ', prices)

# convert each item to int type
for i in range(len(prices)):
    # convert each item to int type
    prices[i] = int(prices[i])
profit=0
prices_copy=prices
profit_list=[]


for i in range(len(prices)):
    for j in range(len(prices_copy)):
        if prices_copy[j] > prices[i] and j>i:
            profit = prices_copy[j] - prices[i]
            profit_list.append(profit)
            profit = 0
	    


if len(profit_list)==0:
    profit = 0
    print('The max profit is ' + str(profit))

else:
    print(('The max profit is ' + str(max(profit_list))))
    
