price1 = 3.14159
price2 = -987.65
price3 = 12.34

# .(number)f - to round tp specific decimal places
print(f"Price 1 is {price1:.2f}") #Price 1 is 3.14

# :(number) - allocate num of spaces
print(f"Price 2 is {price2:10}") #Price 2 is    -987.65

# :0(number) preceed a number with 0 (ero padded)
print(f"Price 3 is {price3:07}")

# :<(number) to left ustify a value
print(f"Price 3 is {price3:<10}") #Price 3 is 12.34     

number = 100000
print(f"The value is {number:,}") #The value is 100,000
print(f"The value is {number:,.2f}") #The value is 100,000.00