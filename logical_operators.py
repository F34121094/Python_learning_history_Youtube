temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad outside")
    print("Stay inside")
elif not(temp < 0 or temp >30):
    print("The temperature is good outside")
    print("Go outside!")
