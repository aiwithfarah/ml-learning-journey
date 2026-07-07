voter_age = int(input("Enter your age: "))

if voter_age >= 18:
    print("You are an adult. You can vote!")
elif voter_age <= 0:
    print("Incorrect age entered!")
else:
    print("You are a minor. You cannot vote!")