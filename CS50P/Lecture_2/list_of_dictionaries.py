students = [
    {'name' : 'farah',
     'house' : 'lukes',
     'patronus' : 'beaver',
     },
    {'name' : 'sana',
     'house' : 'johns',
     'patronus' : 'husky',
     },
    {'name' : 'rusu',
     'house' : 'mathews',
     'patronus' : None,
     },
]

print(students[1]) #{'name': 'sana', 'house': 'johns', 'patronus': 'husky'}

# iterate over list of dictionaries
for student in students:
    print(student['name'])

# farah
# sana
# rusu


for student in students:
    print(student['name'], student['house'], student['patronus'], sep=" | ")
    
# farah | lukes | beaver
# sana | johns | husky
# rusu | mathews | None