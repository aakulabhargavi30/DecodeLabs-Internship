# Expense Tracker

total = 0

print("===== Expense Tracker =====")
print("Enter your expenses one by one.")
print("Type 'done' when you are finished.\n")

while True:
    expense = input("Enter expense: ")

    if expense.lower() == "done":
        break

    try:
        total += float(expense)
    except ValueError:
        print("Please enter a valid number or 'done'.")

print("\n===== Summary =====")
print(f"Total Spent: ₹{total:.2f}")