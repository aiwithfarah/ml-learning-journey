foods = []
prices = []
total = 0

# Ask user what foods they would like to buy

while True:
    food = input("What food would you like to buy? [press 'q' to exit]: ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price) 

print("-----YOUR CART-----")

for i in range(len(foods)):
    print(f"{foods[i]} : ${prices[i]:.2f}") 
           
for price in prices:
    total += price

print()
print(f"Your cart total is: ${total:.2f}")