capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

#print(capitals["Russia"])
# print(capitals.get("Germany"))
# print(capitals.keys())#顯示索引
# print(capitals.values())#顯示內容
# print(capitals.items())#輸出所有東西
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"}) #也可以用來更改內容
capitals.pop("China")

for key,value in capitals.items():
     print(key,value)    #輸出整個字典

