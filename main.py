import json

with open("expenses.json", "r") as file:
    expenses = json.load(file)

def show_expenses(expenses):
     for expense in expenses:
        print(
            f"Name: {expense['name']} - Amount: {expense['amount']} - "
            f"Category: {expense['category']}"
        )

def find_expense(expenses, name):
    for expense in expenses:
        if expense["name"].lower() == name.lower():
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

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    name = input("Enter name of expense? ")
    
    if not name:
        print("Name cannot be empty.")
        return

    try:
        amount = int(input("Enter amount of expense? "))

    except ValueError:
        print("Invalid amount. Please enter a number. ")
        return

    category = input("Enter category of expense? ")

    if not category:
        print("Category cannot be empty.")
        return
    
    if find_expense(expenses, name):
        print("Expense already exists.")
        return

    new_expense = {
        
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added.")

def total_expenses(expenses):
    total = 0
    for expense in expenses:
            total += expense['amount']
    return total
        