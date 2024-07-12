student = [100,90,80,70,60,50,40,30,0]

# pass_student = list(filter(lambda x : x >= 60 , student))

passed_student = [i if i >= 60 else "FAILED"for i in student ]
print(passed_student)