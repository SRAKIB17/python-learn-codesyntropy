binary = input("enter a binary value: ")
length = len(binary)
i = range(0, length)
decimal = 0
for x in i:
    int_value = int((binary[length - x - 1]))
    current = pow(2, x) * int_value
    decimal += current
    # decimal = decimal + current

print(decimal)
