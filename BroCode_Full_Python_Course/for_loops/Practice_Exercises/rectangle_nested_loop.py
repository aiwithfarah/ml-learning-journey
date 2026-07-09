rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")


for row in range(rows):
    for col in range(cols):
        print("*", end=" | ")
    print()