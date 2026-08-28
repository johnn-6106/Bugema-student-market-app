# Bugema Student Market App
# Simple Python program for managing clients, orders and transactions

import json


# Class for Client
class Client:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# Class for Order
class Order:

    def __init__(self, client_name, product, quantity, price):
        self.client_name = client_name
        self.product = product
        self.quantity = quantity
        self.price = price

    # Calculate total bill
    def get_total(self):
        return self.quantity * self.price


# List for storing clients and orders
clients = []
orders = []


# Function for registering a client
def register_client():

    print("\n--- Register Client ---")

    try:
        name = input("Enter client name: ")
        phone = input("Enter phone number: ")

        if name == "" or phone == "":
            print("Name and phone cannot be empty.")
            return

        client = Client(name, phone)

        clients.append({
            "name": client.name,
            "phone": client.phone
        })

        print("Client registered successfully.")

    except Exception as e:
        print("Error occurred:", e)


# Function for creating an order
def create_order():

    print("\n--- Create Order ---")

    try:
        client_name = input("Enter client name: ")
        product = input("Enter product name: ")

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if quantity <= 0 or price <= 0:
            print("Quantity and price must be greater than zero.")
            return

        order = Order(client_name, product, quantity, price)

        orders.append({
            "client": order.client_name,
            "product": order.product,
            "quantity": order.quantity,
            "price": order.price,
            "total": order.get_total()
        })

        print("Order created successfully.")
        print("Total Bill:", order.get_total())

    except ValueError:
        print("Invalid input. Please enter numbers for quantity and price.")

    except Exception as e:
        print("Something went wrong:", e)


# Function to display clients
def view_clients():

    print("\n--- Registered Clients ---")

    if len(clients) == 0:
        print("No clients registered.")
    else:
        for client in clients:
            print("Name:", client["name"])
            print("Phone:", client["phone"])
            print("------------------")


# Function to display orders
def view_orders():

    print("\n--- Transaction Records ---")

    if len(orders) == 0:
        print("No orders found.")
    else:
        for order in orders:
            print("Client:", order["client"])
            print("Product:", order["product"])
            print("Quantity:", order["quantity"])
            print("Price:", order["price"])
            print("Total:", order["total"])
            print("------------------")


# Save data into a file
def save_data():

    try:

        data = {
            "clients": clients,
            "orders": orders
        }

        with open("market_data.json", "w") as file:
            json.dump(data, file)

        print("Data saved successfully.")

    except Exception as e:
        print("Error while saving data:", e)


# Retrieve data from file
def load_data():

    global clients
    global orders

    try:

        with open("market_data.json", "r") as file:

            data = json.load(file)

            clients = data["clients"]
            orders = data["orders"]

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("No previous data file found.")

    except Exception as e:
        print("Error while loading data:", e)


# Main menu
def menu():

    while True:

        print("\n===== BUGEMA STUDENT MARKET APP =====")
        print("1. Register Client")
        print("2. Create Order")
        print("3. View Clients")
        print("4. View Transaction Records")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_client()

        elif choice == "2":
            create_order()

        elif choice == "3":
            view_clients()

        elif choice == "4":
            view_orders()

        elif choice == "5":
            save_data()

        elif choice == "6":
            load_data()

        elif choice == "7":
            print("Thank you for using Bugema Student Market App.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
menu()
