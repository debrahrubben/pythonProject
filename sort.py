# students = ['kojo','kwame','yaw','jojo']
# students.sort()
# for i in students:
#     print(i)

# students = ('kojo','kwame','yaw','jojo')
# sorted_students = sorted(students, reverse=False)
# for i in students:
#     print(i)

students = [('kojo', 'F', 87),
             ('yaw', 'E', 27),
             ('ben', 'C', 57),
             ('Ama', 'B', 97),
             ]
grade = lambda grade:grade[1]
# students.sort(key=grade)
sorted_students = sorted(students,key=grade)

for i in students:
    print(i)