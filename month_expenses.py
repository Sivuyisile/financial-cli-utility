#
from datetime import date

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def month_expenses():

    monthly_expenses = {}

    #only asking initially

    loop_control = True

    while loop_control:

        try:

            month_today = date.today()
            this_month = print(month_today.month)

            user_choice = int(input(f"Do you want to add an item to your list for {this_month}?\n1 for 'Yes'\n2 for 'No':\n"))

            if user_choice == 2:
                loop_control = False
                print("See ya later!")
            elif user_choice == 1:
                pass


            while user_choice == 1:

                user_exps_item = input("Enter the expense title/name: ").lower
                raw_user_exps_amount = input("Enter the item's price: ").strip()
                user_exps_amount = Decimal(raw_user_exps_amount)

                while True:
                    try:
                        user_exps_qty = int(input("Enter the item's quantity: "))

                        if user_exps_qty < 0:
                            print("Error: The item's quantity cannot be negative.")
                            continue
                        if user_exps_qty > 1:
                            user_exps_amount *= user_exps_qty       #feature 1.5 (did this immediately after 1.1)
                            break
                    except ValueError:
                        print("Please enter a whole number")
                        continue

                if user_exps_amount < 0:
                    print("Error: The item cannot have a negative price.")
                    continue

                if user_exps_item in monthly_expenses:
                    print(f"{user_exps_item} already exists, valued at {user_exps_amount}.")

                    #feature/functionality 1.1
                    override_price_value = int(input("Do you wish to change this item's price?\n1 for 'Yes':\n2 for 'No':\n"))

                    if override_price_value == 2:
                        pass
                    elif override_price_value == 1:
                        raw_user_exps_amount = input("Enter the item's new price: ").strip()
                        user_exps_amount = Decimal(raw_user_exps_amount)
                        monthly_expenses[user_exps_item] = user_exps_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                else:
                    monthly_expenses[user_exps_item] = user_exps_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


                user_choice = int(input(f"Do you wish to add another item for {this_month}?\n1 for 'Yes':\n2 for 'No':\n")) #feature 1.3
                #"do you with to add another item for {this_month}?"
                #how will {this_month} be retrieved? by using datetime to get it - DONE

            print(monthly_expenses)

            return monthly_expenses

        except InvalidOperation:
            print("uh oh...Some kind of error")

if __name__ == "__main__":
    month_expenses()
