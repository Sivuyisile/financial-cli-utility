#
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def month_expenses():

    fixed_monthly_expenses = {}
    user_purchases_this_month = []

    #only asking initially

    loop_control = True

    while loop_control:

        try:

            user_choice = int(input("Do you want to add an item to your list for this month?\n1 for 'Yes'\n2 for 'No':\n"))

            if user_choice == 2:
                loop_control = False
                print("See ya later!")
            elif user_choice == 1:
                pass


            while user_choice == 1:

                user_exps_item = input("Enter your fixed monthly expense title/name: ").lower
                raw_user_exps_amount = input("Enter the amount: ").strip()
                user_exps_amount = Decimal(raw_user_exps_amount)

                if user_exps_amount < 0:
                    print("Error: The item cannot be have a negative cost.")
                    continue

                if user_exps_item in fixed_monthly_expenses:
                    print(f"{user_exps_item} already exists, valued at {user_exps_amount}.")
                else:
                    fixed_monthly_expenses[user_exps_item] = user_exps_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

                #feature 1.1
                #I might want to add functionality  to:
                    #override just the value
                    #override both key and value
                    #replace it (which is lowkey the second point/bullet/hash still)

                user_choice = int(input("Do you wish to add another item for this month?\n1 for 'Yes':\n2 for 'No':\n")) #feature 1.3
                #"do you with to add another item for {this_month}?"
                #how will {this_month} be retrieved? by using datetime to get it

            print(fixed_monthly_expenses)

            return fixed_monthly_expenses

        except InvalidOperation:
            print("")

if __name__ == "__main__":
    month_expenses()
