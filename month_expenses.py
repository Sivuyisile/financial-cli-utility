#
from datetime import date, datetime

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


category_map = {
    1: "Housing/Rent",
    2: "Utilities",
    3: "Subscriptions",
    #key: "Groceries" just not sure how I'll work this one since they can fall under both normal monthly exps and fixed monthly exps
    4: "Other/Uncategorised",
    5: "Add new category",
}

def select_category(category_map):

    for key, val in category_map.items():
        print(f"[{key}] {val}")

    print("\nSelect expense category:\n")


    while True:

        try:

            user_choice = int(input("\nSelection: ").strip())

            if user_choice in category_map and user_choice != 5:
                return category_map[user_choice]

            elif user_choice == 5:

                new_user_cat = input("Enetr your new category name: ").strip().title()

                if not new_user_cat:
                    print("Error: Category name cannot be empty.")
                    continue

                if new_user_cat in category_map.values():
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


def capt_exps_entry(expense_dict, category_list):

	
    chosen_category = select_category(category_list)

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
                if user_exps_qty < 0:
                    print("Error: The item's quantity cannot be negative.")
                    continue
                if user_exps_qty >= 1:
                    user_exps_amount *= user_exps_qty       #feature 1.5 (did this immediately after 1.1)
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
            if override_price_value == 2:
                pass
            elif override_price_value == 1:
                raw_user_exps_amount = input("Enter the item's new price: ").strip()
                user_exps_amount = Decimal(raw_user_exps_amount)
                expense_dict[(chosen_category, user_exps_item)] = user_exps_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        else:
            expense_dict[(chosen_category, user_exps_item)] = user_exps_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        ##
        now = datetime.now()
        this_month = now.strftime("%B %Y")
        ##

        user_choice = int(input(f"Do you wish to add another item for {this_month}?\n1 for 'Yes':\n2 for 'No':\n")) #feature 1.3
        #"do you with to add another item for {this_month}?"
        #how will {this_month} be retrieved? by using datetime to get it - DONE
        if user_choice == 2:
            pass
        if user_choice == 1:
            chosen_category = select_category(category_list)
            continue
        else:
            break      #I almost forgot to break out of the loop and exit cleanly




def month_expenses():

    monthly_expenses = {}

    #only asking initially

    loop_control = True

    while loop_control:

        try:

            now = datetime.now()
            this_month = now.strftime("%B %Y")

            user_choice = int(input(f"Do you want to add an item to your list for {this_month}?\n1 for 'Yes'\n2 for 'No':\n"))

            if user_choice == 2:
                loop_control = False
                print("See ya later!")
            elif user_choice == 1:
                capt_exps_entry(monthly_expenses, category_map)

            print("\nCurrent Overview of Expenses:\n")
            print(monthly_expenses)

        except InvalidOperation:
            print("uh uuhh...Please enter 1 or 2.")


    return monthly_expenses


if __name__ == "__main__":
    month_expenses()
