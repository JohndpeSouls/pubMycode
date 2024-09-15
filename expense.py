import os
import json


 # logic for saving the inputs credits to the family of Paris's parents
def load_data(filename):
    if not os.path.exists(filename):
        data = {"total_balance": 0, "income_list": [0, 0, 0, 0, 0], "expenses_list": [0, 0, 0, 0, 0], "initial_balance": 0}
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Created new JSON file: {filename}")
    else:
        print(f"JSON file already exists: {filename}")

    with open(filename, "r") as file:
        data = json.load(file)

    # Ask the user if they want to override the current balance
    override = input("Would you like to override the current balance? (y/n): ").lower()
    if override == 'y':
        new_balance = float(input("Enter your new balance: "))
        data["total_balance"] = new_balance
        data["initial_balance"] = new_balance

    return data
# Function to update the JSON file
def save_data(filename, data, total_balance, income_list, expenses_list, initial_balance):
    with open(filename, "w") as file:
        data["total_balance"] = total_balance
        data["income_list"] = income_list
        data["expenses_list"] = expenses_list
        data["initial_balance"] = initial_balance
        json.dump(data, file)


# Function to handle income
def add_income(data):
    income_action = input('\n───── ⋆⋅☆⋅⋆ ─────\nADD INCOME\n\nChoose a category:\n1. Allowance\n2. Work\n3. Business\n4. Investment\n5. Others\nInput Here (Input number only): ')
    if income_action in ['1', '2', '3', '4', '5']:
        category_index = int(income_action) - 1
        amount = float(input('Enter Amount: '))
        data["income_list"][category_index] += amount
        data["total_balance"] += amount
    return data

# Function to handle expenses (separated as requested)
def add_expenses(data):
    expenses_action = input("\n───── ⋆⋅☆⋅⋆ ─────\nADD EXPENSES\n\nChoose a category:\n1. Food\n2. Transportation\n3. School Stuff\n4. Investment\n5. Others\nInput Here (Input number only): ")
    if expenses_action in ['1', '2', '3', '4', '5']:
        category_index = int(expenses_action) - 1
        amount = float(input('Enter Amount: '))
        data["expenses_list"][category_index] += amount
        data["total_balance"] -= amount
    return data

# Function to check balance
def check_balance(data):
    print("\n───── ⋆⋅☆⋅⋆ ─────\nCURRENT BALANCE: ", data["total_balance"])

# Function to display summary
def display_summary(data):
    total_income = sum(data["income_list"])
    total_expenses = sum(data["expenses_list"])
    i_percentages = [int((amount * 100) / total_income) if total_income else 0 for amount in data["income_list"]]
    e_percentages = [int((amount * 100) / total_expenses) if total_expenses else 0 for amount in data["expenses_list"]]

    print("\n───── ⋆⋅☆⋅⋆ ─────\nSUMMARY OF EXPENSES\n")
    print("\nINITIAL BALANCE: ", data["initial_balance"])
    print("\nTOTAL INCOME: ", total_income)
    print(f"\nAllowance: {data['income_list'][0]} ({i_percentages[0]}%)")
    print(f"Work: {data['income_list'][1]} ({i_percentages[1]}%)")
    print(f"Business: {data['income_list'][2]} ({i_percentages[2]}%)")
    print(f"Investment: {data['income_list'][3]} ({i_percentages[3]}%)")
    print(f"Others: {data['income_list'][4]} ({i_percentages[4]}%)")

    print("\nTOTAL EXPENSES: ", total_expenses)
    print(f"\nFood: {data['expenses_list'][0]} ({e_percentages[0]}%)")
    print(f"Transportation: {data['expenses_list'][1]} ({e_percentages[1]}%)")
    print(f"School Stuff: {data['expenses_list'][2]} ({e_percentages[2]}%)")
    print(f"Investment: {data['expenses_list'][3]} ({e_percentages[3]}%)")
    print(f"Others: {data['expenses_list'][4]} ({e_percentages[4]}%)")

# Main program function
def main():
    filename = "expenses_data.json"
    data = load_data(filename)
    action = 0

    # Loop through actions until 5 is chosen
    while action != 5:
        action = int(input("\n───── ⋆⋅☆⋅⋆ ─────\nChoose Action:\n1. Check Balance\n2. Add Income\n3. Add Expenses\n4. Check Summary\n5. Stop the Program\nInput Here (Type the number only): "))

        if action == 1:
            check_balance(data)
        elif action == 2:
            data = add_income(data)
        elif action == 3:
            data = add_expenses(data)
        elif action == 4:
            display_summary(data)
        elif action > 5:
            print("\nInvalid input. Please choose only from 1-5.")

    # Save data back to the JSON file before exiting
    with open(filename, "w") as file:
        json.dump(data, file)
    print("Program Stopped.")

# Run the program
if __name__ == "__main__":
    main()
