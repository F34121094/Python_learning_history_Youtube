import os
path = "copy.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not there")
except PermissionError:
    print("You are not permission to do that")