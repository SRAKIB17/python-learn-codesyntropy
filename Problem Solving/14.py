x = "level"
# MOM, NUN, 123321
user_input = input("Enter a palindrome text: ")

palindrome = ''
for string in user_input:
    palindrome = string + palindrome

if (user_input == palindrome):
    print("Palindrome")
else:
    print("not Palindrome")
