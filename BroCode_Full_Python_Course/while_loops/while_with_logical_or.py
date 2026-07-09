num = int(input("Enter a number betwwen 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is invalid!")
    num = int(input("Enter a number between 1 and 10: "))

print(num)