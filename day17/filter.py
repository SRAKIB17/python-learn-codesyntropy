# x = filter()
# # filter object
# list(x)/tuple/set
# # index, 012345
def test(itm):
    return itm + 10


x = map(test, list(range(0, 100)))
print(list(x))
