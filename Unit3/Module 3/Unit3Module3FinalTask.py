# [ ] Use the `inventory` dictionary in a program that asks the user for a
#     UPC number, description, unit price, quantity in stock.
# If the item already exists in the inventory, the information is updated,
#     and your program should display a message that it is updating the entry.
# If the item does NOT exists in the inventory, a new dictionary entry is created,
#     and your program should display a message that it is creating a new entry.
# Use try/except in the program.


# test cases

# For an existing item
'''
Enter UPC number: 839529
Enter item description: TOMATOS 1LB
Enter unit price: 1.55
Enter item quantity: 21
Existing item, updating: ['TOMATOS 1LB', 1.29, 25]

  UPC   | Description       |  Unit Price  |  Quantity
-------------------------------------------------------
839529  | TOMATOS 1LB       |         1.55 |      21.00
'''

# For a new item
'''
Enter UPC number: 29430
Enter item description: ORANGE 1LB
Enter unit price: 0.99
Enter item quantity: 40
New item, creating ORANGE 1LB

  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
29430   | ORANGE 1LB        |         0.99 |      40.00
'''

inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}


# get UPC from user, handling cases where the input is invalid with try/except
#TODO: Your code goes here
def get_data(inventory):

    while True:
        try:
            upc = input("Enter UPC number: ")
            if not upc.isdigit():
                raise ValueError("UPC must be numeric value")
            elif len(str(upc)) != 6:
                raise ValueError("UPC must be exactly 6 digits long")
            else:
                pass

            description = input("Enter item description: ").upper()
            if len(description) < 5:
                raise ValueError("Description must be at least 5 characters long")
            else:
                pass

            price = input("Enter unit price: ")
            if isinstance(price, (int, float)):
                raise ValueError("Price must be written in a numeric expression")
            else:
                pass

            quantity = input("Enter item quantity: ")
            if not quantity.isdigit():
                raise ValueError("Quantity must be written in a numeric expression")
            else:
                pass

        except ValueError as theError:
            print(theError)
            pass
        else:
            upc = int(upc)
            description = str(description)
            price = float(price)
            quantity = int(quantity)
            temp = [description, price, quantity]
            message_print(upc, temp, inventory)
            break

# display message, either "updating" or creating" and then item is being updated display the `value` being updated
#TODO: Your code goes here
def message_print(upc, list, main_list):
    value = update_stuff(upc, list, main_list)
    if value == "Update":
        print("Existing item, updated values: {0}".format(main_list[upc]))
    elif value == "New":
        print("New item, creating {0}".format(main_list[upc][0]))
    else:
        pass
    print("UPC     |  Description       |  Unit Price  |  Quantity")
    print("o" + 53 * '-' + "o")
    for key, the_list in main_list.items():
        print(str(key) + (8 - len(str(key))) * " " + "  |  " +
              str(the_list[0]) + (18 - len(str(the_list[0]))) * " " + "|  " +
              str(the_list[1]) + (12 - len(str(the_list[1]))) * " " + "|  " + str(the_list[2]))


# update dictionary entry
#TODO: Your code goes here
def update_stuff(upc, list, main_list):

    for key in main_list.keys():
        if key == upc:
            main_list[key] = list
            return "Update"
        else:
            continue

    main_list[upc] = list
    return "New"

# print header including
# HINT: look at the testing samples shown in comments above for new item and for existing item
#TODO: Your code goes here
def test1(inventory):

    upc = 839529
    temp = ['TOMATOS 1LB', 1.29, 25]
    message_print(upc, temp, inventory)

# print actual data from the dictionary (See Hint above)
#TODO: Your code goes here
def test2(inventory):

    upc = 29430
    temp = ['ORANGE 1LB', 0.99, 40]
    message_print(upc, temp, inventory)


test1(inventory)
test2(inventory)
get_data(inventory)
