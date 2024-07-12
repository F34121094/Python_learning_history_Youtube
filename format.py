animal = "cow"
item = "moon"

print("The {} jump over the {}".format(animal,item))
#format也可以改成直接填入藥輸出的東西ex:cow
print("The {1} jump over the {0}".format(animal,item))
#更改{}裡面的數字可以照裡面的數字來排
print("The {animal} jump over the {item}".format(animal="cow",item="moon"))
#也可以用這種方式來寫
text = "The {} jumped over the {}"
print(text.format(animal,item))
#也可以先把句子定義成一個變數，然後再輸出時把要打進去的填入
