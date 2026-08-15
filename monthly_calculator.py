#
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from income import get_income, check_two_decimals

def monthly_calc():

    fixed_monthly_expenses = {}
    user_purchases_this_month = []

    #only asking initially
    while True:
        try:

            print(fixed_monthly_expenses)

            user_exps_item = input("Enter your fixed monthly expense title/name: ")
            raw_user_exps_amount = input("Enter the amount: ").strip()
            user_exps_amount = Decimal(raw_user_exps_amount)

            check_two_decimals(user_exps_amount)
            
            fixed_monthly_expenses[user_exps_item] = user_exps_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        except InvalidOperation:
            print("")

if __name__ == "__main__":
    monthly_calc()
