x = {
    "name": "Python",
    "version": 3.12,
    "popular": 2
}

#! fromkeys
# form_keys = ["apple", "banana", "watermelon"]
# value = "value"
# x = {}
# for i in form_keys:
#     x.update({
#         i: value
#     })
# print(x)
# print(x.fromkeys(form_keys, "value"))

# * Copy ;
# y = x.copy()
# y.popitem()
# print(y)
# print(x)
# ? get(key_name, default_value=optional)
""" Access item
"""
# print(x["nm"])
# print(x.get("nm"))

# ? items
# print(x.items())
# print(dir(dict))
#! keys()
# print(x.keys())

#! Values
# print(x.values())
#! Update
# x.update({
#     "popular_package": ["Pandas", "Numpy", "Django", "Tensorflow", "Keras", "Pytorch", "openCv"]
# })


# def description():
#     pass


# x.update({
#     "description": description
# })

#  'clear', 'copy', 'fromkeys', 'get', '
# ! Pop => remove item
# print(x.pop('name'))
# print(x)
# ! popitem
# print(x.popitem())
# print(x)


# ! Error Handling:
user_choice = "name"

try:
    print(x[user_choice])
except:
    print("Something is wrong")
finally:
    print("Finally code run")
