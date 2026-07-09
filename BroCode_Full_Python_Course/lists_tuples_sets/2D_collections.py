fruits = ["apple", "banana", "cherry"]
veggies = ["brocoli", "beans", "asparagus"]
meats = ["chicken", "mutton", "fish"]

groceries = [fruits, veggies, meats]
print(groceries)

# accessing element in a 2D list eg: beans
print(groceries[1][1]) #beans

# Iterate over elements of a 2D List use Nested Loops
for items in groceries:
    for item in items:
        print(item) 