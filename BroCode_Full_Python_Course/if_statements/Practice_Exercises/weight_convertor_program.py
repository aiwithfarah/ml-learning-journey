weight = float(input("Enter the weight: "))
unit = input("Is this weight in kgs or lbs: ").lower()

if unit == "kgs":
    weight = weight * 2.20
    print(f"Your weight is {round(weight,2)} {unit}")
elif unit == "lbs":
    weight = weight / 2.20
    print(f"Your weight is {round(weight,2)} {unit}")
else:
    print(f"{unit} is not a valid unit")

