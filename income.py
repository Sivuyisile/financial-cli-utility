from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def get_income(): #ensuring the income is always in 2 decimals

    while True:
        try:

            raw_user_income = input("Income: ").strip()
            user_income = Decimal(raw_user_income)

            if user_income < 0:
                print("Error: Income cannot be negative.")
                continue #this restarts the while loop

            quantised_income_val = user_income.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            #print(set_income_var)

            return quantised_income_val
            
        except InvalidOperation:
            print("Invalid input. Please enter a valid numeric amount.")

if __name__ == "__main__":
    get_income()                                        

#I will ofcourse need to store all of this somewhere