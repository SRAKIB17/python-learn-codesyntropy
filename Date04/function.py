# Function:

def welcome_message(name):
    return "Hello, " + name + ". How are you?"


def good_bye_message(name):
    return "Good Bye " + name + ". See you letter"


message = input("Enter a message:   ")
name = input("Enter your name:  ")

if (message == 'welcome'):
    m = welcome_message(name)
    print(m)
elif (message == 'bye'):
    m = good_bye_message(name)
    print(m)
else:
    print("No function call here")
