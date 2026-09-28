from decimal import Decimal, InvalidOperation
from datetime import datetime

def select_category_prompt(category_map):       #build strictly as a CLI interface situation/component at the moment

    for key, val in category_map.items(): 
        print(f"[{key}] {val}")

    print("\nSelect expense category:\n")

    while True:

        try:

            user_choice = int(input("\nSelection: ").strip())       

            if user_choice in category_map and user_choice != 6:     
                return category_map[user_choice]

            elif user_choice == 6:

                new_user_cat = input("Enter your new category name: ").strip().title()      

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


def exps_entry_prompt(expense_dict, category_list):

    chosen_category = select_category_prompt(category_list)
    this_month = datetime.now().strftime('%B %Y')

    while True:
    
        user_exps_item = input(f"Enter the expense title/name for your '{chosen_category}' expense: ").strip().lower()

        while True:
            try:
                raw_user_exps_amount = input("Enter the item's price: ").strip()
                user_exps_amount = Decimal(raw_user_exps_amount)
                if user_exps_amount < 0:
                    print("Error: An item's price cannot be negative.")
                    continue
                break
            except InvalidOperation:
                print("Error: Please enter a valid price.")
                continue

        while True:
            try:
                user_exps_qty = int(input("Enter the item's quantity: "))

                if not user_exps_qty:
                    print("Error: The item's quantity must be at least 1.")
                    continue
                elif user_exps_qty < 0:
                    print("Error: An item's quantity cannot be negative.")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a whole number")
                continue

        if (chosen_category, user_exps_item) in expense_dict:

            existing_val = expense_dict[(chosen_category, user_exps_item)]
            print(f"{user_exps_item} already exists, valued at {existing_val}.")

            while True:

                #feature/functionality 1.1
                override_price_value = input("Do you wish to change this item's price?\n1 for 'Yes':\n2 for 'No':\n").strip().lower()

                if override_price_value in ('1', 'yes'):
                    while True:
                        raw_user_exps_amount = input("Enter the item's new price: ").strip()  

                        try:
                            user_exps_amount = Decimal(raw_user_exps_amount)

                            if user_exps_amount < 0:
                                print("Error: The item cannot have a negative price.")
                                continue
                            break
                        except InvalidOperation:
                            print("Error: Please enter a valid price.")

                    break   #leaving the override choice loop

                elif override_price_value in ('2', 'no'):
                    break
                else:
                    print("Error: Invalid input. Please enter '1' or '2'.")

                    

        this_month = datetime.now().strftime("%B %Y") 

        while True:
            user_choice = input(f"Do you wish to add another item for {this_month}?\n1 for 'Yes':\n2 for 'No':\n").strip().lower()

            if user_choice in ('1', 'yes'):
                return user_exps_amount, user_exps_item, user_exps_qty, chosen_category, True
            elif user_choice in ('2', 'no'):
                return user_exps_amount, user_exps_item, user_exps_qty, chosen_category, False
            else:
                print("Error: Please enter '1' or '2'.")    