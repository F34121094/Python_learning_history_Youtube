import random #要import的東西不能當成檔案名稱

x = random.randint(1,6)
y = random.random()

myList = ["rock","paper","scissors"]
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)#shuffle為將元素隨機打亂

print(cards)