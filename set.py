utensils = {"fork", "spoon","knife"}
#大括號不能用相同的字
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.update(dishes) #把一個字串加到另一個字串裡
dinner_table = utensils.union((dishes)) #union集合

print(dishes.difference(utensils)) #輸出dishes有但utensils沒有的
print(dishes.intersection(utensils)) #intersection輸出同樣的

#for x in dinner_table:
  #  print(x)