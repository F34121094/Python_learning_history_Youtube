name = "Bro Code"

first_name = name[:3]
last_name = name[4:8]
fucky_name = name[::2] #也可以寫成[0:8:2]，沒寫python會假設從頭輸出到尾
reverse_name = name[::-1] #這樣可以寫出反的
#[start:stop:step]
#沒有打第一個python會假設他是0然後從第一個開始輸出

#print(reverse_name)

website = "http://google.com"

slice = slice(7,-4) #-4但表輸出到倒數第四個
#slice的用法跟[]差不多
print(website[slice]) #變數[slice](其實slice也是一種變數)