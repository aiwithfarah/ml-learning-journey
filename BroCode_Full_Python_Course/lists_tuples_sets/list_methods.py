house = ["mathews", "marks", "lukes", "johns"]

house.append("Rube")

print(house) #['mathews', 'marks', 'lukes', 'johns', 'Rube']    

house.remove("marks")

print(house) #['mathews', 'lukes', 'johns', 'Rube']

house.insert(0, "batool")
print(house) #['batool', 'mathews', 'lukes', 'johns', 'Rube']

house.sort()
print(house) #['Rube', 'batool', 'johns', 'lukes', 'mathews']

house.reverse()
print(house) #['mathews', 'lukes', 'johns', 'batool', 'Rube']

print(house.index("Rube")) #4

house.clear()
print(house) #[]

new_house = ["mathews", "batul", "marks", "lukes", "johns", "lukes"]
print(new_house.count("lukes")) #2
