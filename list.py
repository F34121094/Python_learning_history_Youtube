food = ["pizza","hamburger","hot_dog","spaghetti"]
#print(food[1]) #從0開始，沒有第四個
#print(food[0])

food[0]='sushi'

#(food[0])

#food.append("ice_cream") #在最尾端添加一個元素
#food.remove("hot_dog")
#food.pop() #移除最後一個字元
#food.insert(0,"cake")#插入一個
food.sort()
food.clear()#清除

for x in food:
    print(x)
