# Personal Expense Tracker

A simple command-line expense tracker built with Python.

## Features

* Show all expenses
* Find an expense by name
* Add a new expense
* Remove an expense
* Calculate total expenses
* Prevent duplicate expenses
* Validate user input
* Save expenses to JSON
* Load expenses when the program starts

## Technologies

* Python
* JSON

## How It Works

Expenses are stored as dictionaries inside a Python list.

Each expense contains:

```python
{
    "name": "Food",
    "amount": 500,
    "category": "Groceries"
}
```

The expense data is saved in `expenses.json` so that changes remain available when the program is run again.

## Running the Program

Make sure Python is installed, then run:

```bash
python main.py
```

Follow the menu instructions to manage your expenses.

## What I Learned

This project helped me practice:

* Functions
* Lists and dictionaries
* Loops and conditions
* User input and validation
* `try` / `except`
* JSON data
* Reading and writing files
* Connecting multiple functions into a working program
* Building a menu-driven application
