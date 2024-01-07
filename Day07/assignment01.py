from print_command import print_command
from view_inventory import view_inventory

item_names = ['Laptop', 'Headphones', 'Keyboard', 'Mouse']
item_quantities = [10, 20, 15, 30]
item_prices = [10, 20, 15, 30]

isExit = False
while not isExit:
    command = print_command()
    print(command)
    get_choice = int(input(">Enter your command: "))

    if (get_choice == 1):
        get_inventory_item = view_inventory([
            item_names, item_quantities, item_prices
        ])
        print(get_inventory_item)

    elif (get_choice == 8):
        isExit = True
