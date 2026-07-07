name = input("Enter your full name: ")
mobile_num = input("Enter mobile number: ") #123-456-789

name_length = len(name)
print(f"Your full name has {name_length} characters")

print(name.capitalize()) #Haraf
# find method return the first index (left-most occurance). Starts counting from 0
print(name.find("a")) #1

print(name.rfind("h")) #0

print(name.lower()) #haraf
print(name.upper()) #HARAF
print(name.title()) #Haraf

print(name.isdigit()) #False

print(name.isalpha()) #True

print(mobile_num.count("-")) #2 
print(mobile_num.replace("-", "*")) #123*456*789

print(help(str))