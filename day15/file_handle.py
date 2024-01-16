import os
from pprint import pprint as print
location = "info.txt"
file = open(location, "r")
file.close()
# file.write("hello python. Again writing")
# print(file.readline())
print(file)
os.remove(location)
# info = file.readlines()
# db = dict()
# for x in info:
#     splt = x.split(",")
#     key = splt[0]
#     value = splt[1]
#     db.update({key: value})

# file.write(db)

# file.close()
