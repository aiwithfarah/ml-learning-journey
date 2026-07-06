name = "Haraf"
age = 34
gpa = 2.99
is_learning_python = True

print(type(name))  #<class 'str'>
print(type(age)) #<class 'int'>
print(type(gpa)) #<class 'float'>
print(type(is_learning_python)) #<class 'bool'> 

# type-cast float to int
new_gpa = int(gpa)
print(f"Your new gpa is: {new_gpa}") #Your new gpa is: 2

# type-cast int to float
new_age = float(age)
print(new_age) #34.0

# type-cast string to boolean
new_name = bool(name)
print(new_name) #True