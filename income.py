from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def check_two_decimals(amount):
    
    if amount.as_tuple().exponent < -2:
        print("Error: Income cannot consist of more than two decimal places.")
        #continue

    if amount < 0:
        print("Error: Income cannot be negative.")
        #continue


def get_income(): #ensuring the income is always in 2 decimals

    this_month_income = []

    while True:
        try:

            raw_user_income = input("Income: ").strip()
            user_income = Decimal(raw_user_income)

            check_two_decimals(user_income)

            this_month_income.append(user_income.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

            return this_month_income[0]

        except InvalidOperation:
            print("Invalid input. Please enter a valid numeric amount.")

if __name__ == "__main__":
    get_income()