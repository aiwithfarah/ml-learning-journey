n = int(input("Enter a number: "))

while n < 0:
    print("Number can't be Negative")
    n = int(input("Enter a number: "))
else:
    for _ in range(n):
        print("meow")