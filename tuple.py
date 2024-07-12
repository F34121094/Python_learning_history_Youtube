students = ("Bro",21,"male")

print(students.count("Bro")) #bro是這個裡面的第一個(count用數的)
print(students.index("male"))

for x in students:
    print(x)

if "Bro" in students:
    print("Bro is here!")