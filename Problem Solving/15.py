from pprint import pprint as print

user_input = "Develop a program that counts the Develop frequency of each word in a sentence Develop or paragraph"
split_text = user_input.split()
x = ["apples", "apples"]

# key: value
frequency = {
}

for i in split_text:
    get_key = frequency.get(i)
    if (get_key):
        frequency.update({
            i: get_key+1
        })
    else:
        frequency.update({i: 1})


for key in frequency:
    value = frequency.get(key)
    print(key+": "+str(value))
