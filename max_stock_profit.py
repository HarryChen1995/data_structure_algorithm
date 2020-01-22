
def maximum_stock_price(arr):
    max_profit = 0 
    min_price = float("inf")
    for i in arr:
        if i < min_price:
            min_price = i
        if i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit

print(maximum_stock_price([7,1,5,3,6,4]))
