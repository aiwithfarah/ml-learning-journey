fruits = {"apple", "banana", "cherry"}

print(len(fruits)) #3

print("banana" in fruits) #True

# can't chage values but can add and remove

fruits.remove("apple")
print(fruits) #{'cherry', 'banana'}

fruits.add("guava")
print(fruits) #{'cherry', 'guava', 'banana'}

fruits.clear()
print(fruits) #set()