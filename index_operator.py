name = "bro Code!"

# if(name[0].islower()): #把第一個字變大寫
#     name = name.capitalize()
first_name = name[0:3].upper() #把前三個變大寫
last_name = name[4:].lower() #把後面的變小寫
last_character =  name[-1]

print(last_name)
print(last_character)