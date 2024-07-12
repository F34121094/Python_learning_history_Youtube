rows = int(input("Hoe many rows?: "))
columns = int(input("Hoe many columns?: "))#columns列
symbol = input("Enter a sybol to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #使用end=""可以讓python不進行換行
    print() #在使用一個print()可以讓python換行