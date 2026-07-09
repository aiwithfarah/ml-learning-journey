students = {
    "Dave": "Mathwes",
    "Farah" : "Lukes",
    "Ibjee" : "Johns",
    "Sacchi" : "Marks",
}

print(students['Farah']) #Lukes

# iterate over dict
for student in students:
    print(student, students[student], sep="-")

# Dave-Mathwes
# Farah-Lukes
# Ibjee-Johns
# Sacchi-Marks