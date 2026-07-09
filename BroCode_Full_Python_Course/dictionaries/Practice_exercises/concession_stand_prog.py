# create a menu for movie theater dictionary
menu = {
    'pizza' : 3.99,
    'burger' : 2.50,
    'fries' : 1.50,
    'coke' : 1,
    'popcorn' : 2.99,
}

# list cart containing user selected items
cart = []

#total variable to keep track of the total 
cart_total = 0

# display menu to user using .items(). Format using formal sepcifiers
print('-------MENU-------')
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")
#add decorative text before and after the menu
print('------------------')

# ask user what items they would like to buy using while True loop
while True:
    choice = input("What would you like to have?: ['q' to quit] ").lower()
    if menu.get(choice) is not None:
        cart.append(choice)
    elif choice == "q":
        break     

#append selected items to list_cart
# print(cart)
print('-----YOUR ORDER-----')

# calculate total using for loop
for item in cart:
    cart_total += menu[item]
    print(item, end=", ")

print()

print(f"Your total is : ${cart_total:.2f}")