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

    chosen_category = select_category_prompt(category_list).strip().title()
    this_month = datetime.now().strftime('%B %Y')

    while True:
    
        #user_exps_item = input(f"Enter the expense title/name for your '{chosen_category}' expense: ").strip().lower()
        user_exps_item = input(f"Enter the expense title/name for your '{chosen_category}' expense: ").strip().title()

        matching_key = next(((category, item) for category, item in expense_dict.keys() if item.lower() == user_exps_item.lower()), None)

        if matching_key:
            existing_category, existing_item = matching_key
            existing_val, existing_qty = expense_dict[matching_key]

            stored_val = existing_val * existing_qty

            print(f"{user_exps_item} already exists in your {existing_category} category, valued at {stored_val}.")

            ###
            #loop / code block to ask if they want to keep it in the same category, or if they want to move it to their newly/currently chosen category
            if existing_category.lower() != chosen_category.lower():

                while True:

                    move_categories = input(f"Do you wish to move {user_exps_item} from '{existing_category}' to '{chosen_category}'?\n1 for 'Yes':\n2 for 'No':\n").strip().lower()

                    if move_categories in ('1', 'yes'):
                        
                        old_key = (existing_category, existing_item)
                        new_key = (chosen_category, existing_item)

                        expense_dict.pop(old_key) #so as to not have orphaned data after moving the 'key' from its original category to its new one

                        existing_category = chosen_category
                        matching_key = new_key
                        break
                    elif move_categories in ('2', 'no'):
                        #move on to the price loop
                        chosen_category = existing_category
                        break
                    else:
                        print("Please enter '1' for 'Yes', or '2' for 'No':")
                        continue

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
                    break   #leaving the override price choice loop

                elif override_price_value in ('2', 'no'):
                    user_exps_amount = existing_val
                    break
                else:
                    print("Error: Invalid input. Please enter '1' or '2'.")

#while loop here?
            while True:

                override_quantity = input("Do you wish to change/update this item's quantity?\n1 for 'Yes':\n2 for 'No':\n").strip().lower()

                if override_quantity in ('1', 'yes'):
                    while True:
                        raw_user_exps_quantity = input("Enter the item's new quantity: ").strip()

                        try:
                            user_exps_qty = int(raw_user_exps_quantity)

                            if user_exps_qty < 0:
                                print("Error: The item cannot have a negative quantity.")
                                continue
                            break      
                        except ValueError:
                            print("Please enter a valid whole number quantity.")
                    break

                elif override_quantity in ('2', 'no'):
                    user_exps_qty = existing_qty
                    break
                else:
                    print("Error: Invalid input. Please enter '1' or '2'.")


        else:
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


        this_month = datetime.now().strftime("%B %Y") 

        while True:
            user_choice = input(f"Do you wish to add another item for {this_month}?\n1 for 'Yes':\n2 for 'No':\n").strip().lower()

            if user_choice in ('1', 'yes'):
                return user_exps_amount, user_exps_item, user_exps_qty, chosen_category, True
            elif user_choice in ('2', 'no'):
                return user_exps_amount, user_exps_item, user_exps_qty, chosen_category, False
            else:
                print("Error: Please enter '1' or '2'.")    