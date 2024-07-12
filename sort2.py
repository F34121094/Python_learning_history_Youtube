student = [("Squidward","F",60),
           ("Sandy","A",33),
           ("Patrick","B",36),
           ("Spongebbob","B",20),
           ("Mr.krabs","C",78)]

age = lambda student:student[2]
student.sort(key=age,reverse=False)

for i in student:
    print(i)