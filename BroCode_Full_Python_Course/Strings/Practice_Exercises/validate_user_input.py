# 1 User name is no more than 12 char
# 2 User name must not contain spaces
# 3 User name must not vontain digits 

username = input("Enter username:")

if len(username) > 12:
    print("Username cannot be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Your username cannot have spaces")
elif not username.isalpha():
    print("Your username cannot contain digits")
else:
    print(f"Welcome {username}")