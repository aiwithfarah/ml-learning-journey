name = input("Enter your name: ")

while name == "":
    print("You did not enter a name!")
    name = input("Enter a name: ")
print(f"Hello {name}")