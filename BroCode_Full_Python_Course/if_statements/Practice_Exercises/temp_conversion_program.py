unit = input("Celcius or Farhenheit - [C / F]: ").lower()
temp = float(input("Enter Temp: "))

if unit == "c":
    new_temp = (9 * temp) / 5 + 32
    print(f"{temp}{unit} in Farhenheit is {round(new_temp,2)}F")
elif unit == "f":
    new_temp = (temp - 32) * 5 / 9
    print(f"{temp}{unit} in Celcius is {round(new_temp,2)}C")

else:
    print(f"{unit} is not a valid unit")