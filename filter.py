friends = [
    ('Rubben',23),
    ('Ama',3),
    ('Kojo',234),
    ('Prince',203)
]
age = lambda data:data[1] >= 18
drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)