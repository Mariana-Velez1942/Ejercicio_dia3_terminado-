
# Inventory Management System for a store
# This program allows a store inventory manager to add, search, update, delete products,
# and also calculate the total value of the current inventory in a very easy way.
# All the information about the products like name, price and quantity is stored in a dictionary.

# This is the dictionary where we will save all the products
inventory = {}

# This function adds a product to the inventory
def add_product(product_name, product_price, product_quantity):
    # We use the product name as the key in the dictionary
    inventory[product_name] = {
        "price": product_price,
        "quantity": product_quantity
    }

# This function searches for a product in the inventory
def search_product(product_name):
    if product_name in inventory:
        product = inventory[product_name]
        print(f"Name: {product_name}, Price: ${product['price']}, Quantity: {product['quantity']}")
    else:
        print("This product does not exist in the inventory.")

# This function updates the price of an existing product
def update_product_price(product_name, new_price):
    if product_name in inventory:
        if new_price > 0:
            inventory[product_name]["price"] = new_price
            print("The price has been updated successfully.")
        else:
            print("The new price must be a positive number.")
    else:
        print("This product does not exist in the inventory.")

# This function deletes a product from the inventory
def delete_product(product_name):
    if product_name in inventory:
        del inventory[product_name]
        print("The product has been deleted successfully.")
    else:
        print("This product does not exist in the inventory.")

# This function calculates the total inventory value
def calculate_total_inventory_value():
    total_value = 0
    for product in inventory.values():
        total_value += product["price"] * product["quantity"]
    print(f"Total inventory value: ${total_value:.2f}")

# Add 5 initial products to the inventory
add_product("apple", 0.50, 100)
add_product("banana", 0.30, 150)
add_product("orange", 0.40, 120)
add_product("milk", 1.20, 50)
add_product("bread", 1.00, 80)

# This function shows the menu with all the available options
def show_menu():
    print("\nWelcome to the Inventory Management System")
    print("1. Add a new product")
    print("2. Search for a product")
    print("3. Update the price of a product")
    print("4. Delete a product")
    print("5. Calculate total inventory value")
    print("6. Exit the program")

# This loop keeps the program running until the user chooses to exit
while True:
    show_menu()
    option = input("Please choose an option (1-6): ")

    if option == "1":
        name = input("Enter the product name: ")
        try:
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the product quantity: "))
            add_product(name, price, quantity)
            print("Product added successfully.")
        except ValueError:
            print("Please enter valid numbers for price and quantity.")

    elif option == "2":
        name = input("Enter the name of the product to search: ")
        search_product(name)

    elif option == "3":
        name = input("Enter the name of the product to update: ")
        try:
            new_price = float(input("Enter the new price: "))
            update_product_price(name, new_price)
        except ValueError:
            print("Please enter a valid number for the new price.")

    elif option == "4":
        name = input("Enter the name of the product to delete: ")
        delete_product(name)

    elif option == "5":
        calculate_total_inventory_value()

    elif option == "6":
        print("Thank you for using the Inventory Management System. Goodbye!")
        break

    else:
        print("Invalid option. Please select a number between 1 and 6.")
