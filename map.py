store =[("shirt",20.00),
        ("pants",25.00),
        ("jacket",50.00),
        ("socks",10.00)]

to_euros = lambda data:(data[0],data[1]*0.82)
to_USA = lambda data:(data[0],data[1]/0.82)

store_USA = list(map(to_USA,store))

for i in store_USA:
    print(i)