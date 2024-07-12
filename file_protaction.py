import os

path = "C:\\Users\\willy\\Desktop\\folder"

if os.path.exists(path):
    print("exists")
    if os.path.isfile(path):
        print("That's a file")
    elif os.path.isdir(path):
        print("That's a directory")
else:
    print("doesn't exist")