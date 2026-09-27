import json
from unicodedata import category

with open('expenses.json', 'r') as f:
    expenses = json.load(f)

def show_expenses(expenses):
     for expense in expenses:
        print(
            f"Name: {expense['name']} - Amount: {expense['amount']} - "
            f"Category: {expense['category']}"
        )

def find_expense(expenses, name):
    for expense in expenses:
        if expense['name'].lower() == name.lower():
            return expense
    return None
    

def find_and_display_expense(expenses):
    name = input("Enter name of expense? ")
    
    if not name:
        print("Name cannot be empty.")
        return

    expense = find_expense(expenses, name)
    
    if expense:
        print(expense)
    
    else:
        print("Expense not found")

def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

def add_expense(expenses):
    name = input("Enter name of expense? ")
    
    if not name:
        print("Name cannot be empty.")
        return

    try:
        amount = int(input("Enter amount of expense? "))

    except ValueError:
        print("Amount cannot be empty.")
        return

    category = input("Enter category of expense? ")

    if not category:
        print("Category cannot be empty.")
        return

    new_expense = {
    "name": name,
    "amount": amount,
    "category": category
}

    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added.")

def menu(employees):
    choice = ""

    while choice != "5":
        print("\n1. Show employees")
        print("2. Find employee")
        print("3. Add employee")
        print("4. Remove employee")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_employees(employees)

        elif choice == "2":
            find_and_display_employee(employees)

        elif choice == "3":
            add_employee(employees)
            
        elif choice == "4":
            remove_employee(employees)

        elif choice == "5":
            print("Goodbye!")

        else:
            print("Invalid choice")

menu(expenses)