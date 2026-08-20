#
from datetime import date, datetime

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


category_map = {
    1: "Housing/Rent",
    2: "Utilities",
    3: "Subscriptions",
    4: "Groceries",
    5: "Other/Uncategorised",
    6: "Add new category",
}

def item_total_calc(quantity, price):

    if quantity < 1:
        return ValueError("Quantity must at least be 1.")
    elif price < 0:
        return ValueError("Price cannot be negative.")

    return (price * quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def grand_total_calc(expense_dict):

    return sum(expense_dict.values(), Decimal("0.01"))


def add_new_expense_or_update(expense_dict, category, item, amount):

    item_key = (category, item.strip().lower())

    if item_key in expense_dict:
        prev_amount = expense_dict[item_key]
        expense_dict[item_key] = amount
        return True, prev_amount
    
    expense_dict[item_key] = amount
    return False, Decimal("0.01")



def select_category_prompt(category_map):

    for key, val in category_map.items(): #decouple: user
        print(f"[{key}] {val}")

    print("\nSelect expense category:\n")

    while True:

        try:

            user_choice = int(input("\nSelection: ").strip())       #decouple: user

            if user_choice in category_map and user_choice != 6:     #decouple: background
                return category_map[user_choice]

            elif user_choice == 6:

                new_user_cat = input("Enter your new category name: ").strip().title()      #decouple: user

                if not new_user_cat:     #decouple: background
                    print("Error: Category name cannot be empty.")
                    continue

                if new_user_cat in category_map.values():    #decouple: background
                    print(f"{new_user_cat} already exists.")
                    return new_user_cat

                new_key = len(category_map) + 1
                category_map[new_key] = new_user_cat
                print(f"Success: Added '{new_user_cat}' as option [{new_key}]")
                return new_user_cat

            else:
                print("Error: Invalid selection.\nPlease choose from the available numbers.")
                continue

        except ValueError:
            print("Error: Please enter a whole number.")
            continue

#still need to add functionality to allow adding a new category - DONE
#(remember to capitalise the newly added category names accordingly) - DONE (using .title())


def exps_entry_prompt(expense_dict, category_list):

	
    chosen_category = select_category_prompt(category_list)

    while True:
    
        user_exps_item = input(f"Enter the expense title/name for your '{chosen_category}' expense: ").strip().lower()

        try:
            raw_user_exps_amount = input("Enter the item's price: ").strip()
            user_exps_amount = Decimal(raw_user_exps_amount)
        except InvalidOperation:
            print("Error: Please enter a valid price.")

        while True:
            try:
                user_exps_qty = int(input("Enter the item's quantity: "))

                if not user_exps_qty:
                    print("Error: The item's quantity cannot be empty.")
                    continue
                elif user_exps_qty < 0:
                    print("Error: The item's quantity cannot be negative.")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a whole number")
                continue

        if user_exps_amount < 0:
            print("Error: The item cannot have a negative price.")
            continue
        if not user_exps_amount:
            print("Error: The item's amount cannot be empty.")

        if (chosen_category, user_exps_item) in expense_dict:
            print(f"{user_exps_item} already exists, valued at {user_exps_amount}.")

        #feature/functionality 1.1
        override_price_value = int(input("Do you wish to change this item's price?\n1 for 'Yes':\n2 for 'No':\n"))

#checkpoint1: changing how I send the values to the dictionary --> to the 2-named tuple situation
        if override_price_value == 1:
            raw_user_exps_amount = input("Enter the item's new price: ").strip()
            user_exps_amount = Decimal(raw_user_exps_amount)
        if override_price_value != 1:
            break


        ##
        now = datetime.now()
        this_month = now.strftime("%B %Y")
        ##

        user_choice = int(input(f"Do you wish to add another item for {this_month}?\n1 for 'Yes':\n2 for 'No':\n")) #feature 1.3
        #"do you with to add another item for {this_month}?"
        #how will {this_month} be retrieved? by using datetime to get it - DONE
        if user_choice == 1:
            chosen_category = select_category_prompt(category_list)
            continue
        if user_choice == 2:
            return user_exps_amount, user_exps_item, user_exps_qty    #realised I might want to use these later 


def month_expenses():

    monthly_expenses = {}

    this_month = datetime.now().strftime("%B %Y")  #quicker

    print(f"Expense tracker: {this_month}\n")

    while True:

        chosen_category = select_category_prompt(category_map)

        user_exps_amount, user_exps_item, user_exps_qty = exps_entry_prompt() 

        item_total = item_total_calc(user_exps_qty, user_exps_amount)

        is_override, old_val = add_new_expense_or_update(monthly_expenses, chosen_category, user_exps_item, user_exps_amount)

        #saw someone do this - add_new_expense_or_update()
        if is_override:
            return f"Success. Price of {user_exps_item} has been updated from {old_val} to {item_total}"
        else:
            return f"Thank you. {user_exps_item} has been added to {chosen_category} at {item_total}"


if __name__ == "__main__":
    month_expenses()
