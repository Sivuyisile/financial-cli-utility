from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from expenses_cli import exps_entry_prompt

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
        raise ValueError("Quantity must at least be 1.")
    #I have to 'raise' it instead of just returning, as 'return' returns the error object as data
    elif price < 0:
        raise ValueError("Price cannot be negative.")

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
 

def month_expenses():

    monthly_expenses_dict = {}

    this_month = datetime.now().strftime("%B %Y") 

    print(f"Expense tracker: {this_month}\n")

    keep_going = True

    while keep_going:

        user_exps_amount, user_exps_item, user_exps_qty, chosen_category, keep_going = exps_entry_prompt(monthly_expenses_dict,category_map) 

        item_total = item_total_calc(user_exps_qty, user_exps_amount)

        is_override, old_val = add_new_expense_or_update(monthly_expenses_dict, chosen_category, user_exps_item, item_total)

        #saw someone do this - add_new_expense_or_update()
        if is_override:
            print(f"Success. Price of {user_exps_item} has been updated from {old_val} to {item_total}")
        else:
            print(f"Thank you. {user_exps_item} has been added to {chosen_category} at {item_total}")

    return monthly_expenses_dict


if __name__ == "__main__":
    month_expenses()
