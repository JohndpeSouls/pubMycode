# Function to calculate percentage
def calculate_percentage(part, whole):
    return round((part / whole) * 100, 2)

# Page 1: Get savings amount from the user
def get_savings():
    while True:
        try:
            savings = float(input("Enter your total savings amount (e.g., 5000): "))
            if savings < 0:
                print("Savings cannot be negative. Please enter a valid amount.")
            else:
                return savings
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Page 2: Get expense categories and their amounts
def get_expenses(savings):
    categories = {}
    print("\nEnter your 5 expense categories and the amount spent in each:")

    for i in range(1, 6):
        while True:
            category = input(f"Enter name for expense category {i}: ").strip()
            if category in categories:
                print("This category already exists. Please enter a different one.")
                continue

            try:
                amount = float(input(f"Enter the amount spent on {category}: "))
                if amount < 0:
                    print("Expense amount cannot be negative. Please enter a valid amount.")
                elif amount > savings:
                    print("Cannot enter amount thats greater than savings")
                else:
                    categories[category] = amount
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    return categories

# Page 3: Calculate and display percentages
def display_report(savings, expenses):
    total_expenses = sum(expenses.values())
    total_budget = savings + total_expenses

    print("\nExpense Report:")
    for category, amount in expenses.items():
        percentage = calculate_percentage(amount, total_expenses)
        perfent = calculate_percentage(amount, savings)
        print(f"- {category}: {percentage}% of total expenses")
        print(f" - {category}: {perfent}% spent from savings")

    # Calculate and display savings percentage
    savings_percentage = calculate_percentage(savings, total_budget)
    expenses_percentage = calculate_percentage(total_expenses, total_budget)
    savings_spent = calculate_percentage(total_expenses, savings)

    print(f"\nSavings vs Budget:")
    print(f"- Savings: {savings_percentage}% of total budget")
    print(f"- Total Expenses: {expenses_percentage}% of total budget")
    print(f"- Savings spent {savings_spent}% and amount of savings left from your expenses {savings - total_expenses}")

def main():
    # Page 1
    print("Welcome to the Savings and Expenses Calculator")
    savings = get_savings()

    # Page 2
    expenses = get_expenses(savings)

    # Page 3
    display_report(savings, expenses)

if __name__ == "__main__":
    main()
