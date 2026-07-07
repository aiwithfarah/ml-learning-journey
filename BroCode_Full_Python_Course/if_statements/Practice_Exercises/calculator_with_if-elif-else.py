# Select arithematic operator
opeartor = input("Enter an operator: [+, -, *, /, //, %, **]: ")

#Ask for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = 0

# Calculator Logic
if opeartor == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result,2)}")
elif opeartor == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result,2)}")
elif opeartor == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result,2)}")
elif opeartor == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {round(result,2)}")
elif opeartor == "//":
    result = num1 // num2
    print(f"{num1} // {num2} = {round(result,2)}")
elif opeartor == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {round(result,2)}")
elif opeartor == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {round(result,2)}")
else:
    print("Incorrect Operator entered!")