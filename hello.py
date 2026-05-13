#expense tracker
expenses = []
# add an expense to the list
def add_expense(amount, category, description, date):
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    })
# display all expenses    
def display_expenses():
    for expense in expenses:
        print(f"{expense['date']}: {expense['category']} - {expense['description']} (${expense['amount']})")
# categorize expenses by category and display totals
def categorize_expenses():
    categorized = {}
    for expense in expenses:
        category = expense['category']
        categorized[category] = categorized.get(category, 0) + expense['amount']
    for category, total in categorized.items():
        print(f"{category}: ${total}")
# calculate total expenses
def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total}")
# find the highest expense
def highest_expense():
    if not expenses:
        print("No expenses recorded.")
        return
    highest = max(expenses, key=lambda x: x['amount'])
    print(f"Highest Expense: {highest['date']} - {highest['category']} - {highest['description']} (${highest['amount']})")
#search expenses by keyword in category
def search_expenses(keyword):
    results = [expense for expense in expenses if keyword.lower() in expense['category'].lower()]
    if results:
        for expense in results:
            print(f"{expense['date']}: {expense['category']} - {expense['description']} (${expense['amount']})")
    else:
        print("No expenses found matching the keyword.")
#delete an expense by index
def delete_expense(index):
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted Expense: {removed['date']} - {removed['category']} - {removed['description']} (${removed['amount']})")
    else:
        print("Invalid index. No expense deleted.")

#menu for user interaction
def menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Categorize Expenses")
        print("4. Total Expenses")
        print("5. Highest Expense")
        print("6. Search Expenses by Category")
        print("7. Delete Expense")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, description, date)
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            categorize_expenses()
        elif choice == '4':
            total_expenses()
        elif choice == '5':
            highest_expense()
        elif choice == '6':
            keyword = input("Enter category keyword to search: ")
            search_expenses(keyword)
        elif choice == '7':
            index = int(input("Enter the index of the expense to delete: "))
            delete_expense(index)
        elif choice == '8':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")