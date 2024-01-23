# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simpleGeneratorFun():
    for i in range(0, 20):
        yield i


# x is a generator object

x = simpleGeneratorFun()
for i in x:
    print(i)

# Iterating over the generator object using next
# In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))

# a = ["name", 'version', "popular"]
# b = ['python', 3.12, 2]

# print(dict(zip(a, b)))
