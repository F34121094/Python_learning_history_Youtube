try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("The file is not found")
# print(file.closed)