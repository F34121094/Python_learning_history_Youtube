age = int(input("How old are you?: "))

if age >= 18 and age != 100:
    print("You are an adult")
elif age == 100:
    print("You are a century old")
elif age < 0:
    print("You haven't been been yet!")
else:
    print("You are a child")