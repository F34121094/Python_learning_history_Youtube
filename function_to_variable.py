def hello():
    print("Hello")

print(hello)
hi = hello
print(hi)
hi() #剛剛已經把hi定義成hello了，hello現在有2個名字

say = print
say("Wow I can't believe this function")