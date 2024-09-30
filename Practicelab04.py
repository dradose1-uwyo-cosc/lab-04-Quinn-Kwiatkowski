walmart_items = ["Bread","Yogurt","Milk","Pasta","egg"]
walmart_prices = [5.25,5,4,10,2.10]
cost = 0

for i in range(len(walmart_items)):
    print(f"I bought {walmart_items [i]} for ${walmart_prices[i]}")
    cost = cost + walmart_prices[i]

print(f"I spent ${cost} at walmart") #Outside the for loop so that it doesn't print on every iteration

#cheapest item
cheapest = walmart_prices.index(min(walmart_prices))
print(f"The cheapest item was {walmart_items[cheapest]}")
#most expensive item
expensive = walmart_prices.index(max(walmart_prices))
print(f"The most expensive item was {walmart_items[expensive]}")
