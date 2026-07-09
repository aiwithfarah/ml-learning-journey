# A = p(1 + r/n)

principal_amount = 0
rate = 0
time = 0

while principal_amount <= 0:
        principal_amount = float(input("Enter Principal Amount: "))
        if principal_amount <=0:
                print("Principal Amount can't be less than or equal to 0") 
            

while rate <= 0:
        rate = float(input("Enter Rate of iterest: "))
        if rate <=0:
                print("Rate can't be less than or equal to 0") 
            

while time <= 0:
        time = int(input("Enter time in years: "))
        if time <=0:
                print("Time can't be less than or equal to 0") 
            

total = principal_amount * pow((1 + rate/100), time)

print(f"Balance after {time} year/s: {total:.2f}$")

