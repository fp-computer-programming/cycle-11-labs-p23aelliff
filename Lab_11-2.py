#author ate(11/31/23)

#Dictionary
grades = {"Mid Year Proposal": 100/100, "Mid Year Project code": 91/100, "Mid Year Project Reflection": 93/100, "Mid Year Project Presention": 93/100}

#statement for grades recieved
for (values) in grades.values():
    print(values)


#for loop statements for assignments
for k in grades:
    print(k)

#grades above 70%
for (k, v) in grades.items():
    print(k,v)

#grades below 50%
for (k,v) in grades.items():
    print("There are no grades below 50%")