students = [100,90,80,70,60,50,40,30,0]

passed = [i if i >= 60 else "failed" for i in students]
print(passed)