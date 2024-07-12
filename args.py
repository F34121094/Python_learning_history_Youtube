def add(*stuff): #用args(只要使用*即可)就能不管需要寫輸出幾個
    sum = 0
    stuff = list(stuff) #要先用這個才能改裡面的內容
    stuff[0] = 0 #將1改成0
    for i in stuff:
         sum+=i
    return sum

print(add(1,2,3,4,5,6))