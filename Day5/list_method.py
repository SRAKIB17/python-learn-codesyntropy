from pprint import pprint as print
# x = [
#     ["python", '3.12', "interpreted"],
#     ["C", '0.4', "compiler"],
#     ["Java", '1.4', "compiler"],
# ]


x = ["python", '3.12', "interpreted"]

# ! Add a item
# x.append("easy language")
# # insert
# x.insert(0, 'C programming')

# pop
# index দিয়ে
# x.pop(1)

# value দিয়ে
# x.remove('python')
# print(x)

# ! Count item
"""
print(x.count("python"))
"""
y = [1, 2, 3, 5]
# x.extend(y)
# print(x)

# access item:
# print(x[0])

# find index

# print(x.index("python"))


# 1 . list => set
# 2. set => list

# x.reverse()
def sorting_list(n):
    return len(n)


old = ['apple', 'orange', 'banana', 'pineapple']
new = old
new.clear()

old.sort(key=sorting_list, reverse=True)
print("old list")
print(old)
