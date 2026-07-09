fruits = ["grapes", "papaya", "oranges", "watermelon"]

print(fruits[0]) #grapes

# SLICING  : [START : STOP : STEP]

print(fruits[::2]) #['grapes', 'oranges']

reversed_list = fruits[::-1]
print(reversed_list) #['watermelon', 'oranges', 'papaya', 'grapes']

# iterate over lists
for fruit in fruits:
    print(fruit)
# grapes
# papaya
# oranges
# watermelon

# print(dir(fruits))
# print(help(fruits))

print(len(fruits))

print("grapes" in fruits) #True

fruits[0] = "haraf"
print(fruits) #['haraf', 'papaya', 'oranges', 'watermelon']


