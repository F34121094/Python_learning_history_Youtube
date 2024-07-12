name_1 = "ABSC"
name_2 = "willy"
name_3 = "1234"
print(len(name_1))
print(len(name_2))

print(name_2.find("1")) #在字串中找一個字的函示(從0開始)
print(name_2.capitalize()) #將第一個字大寫
print(name_2.upper()) #將所有字大寫
print(name_1.lower()) #將所有字母小寫
print(name_2.isdigit())
print(name_3.isdigit()) #辨識字串是不是數字
print(name_2.isalpha()) #辨識是否只有字母(有空格則顯示False)
print(name_2.count("l")) #len就能用來算字數了 count用來算有幾個特並字母
print(name_2.replace("l","d"))
print(name_2 * 3)