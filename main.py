import json

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
