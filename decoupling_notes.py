##
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

#alright, let's start with decoupling our 'select_category()' function


def select_category(category_map):

     pass

    

def category_cli():

    for key, val in category_map.items(): #decouple: user
            print(f"[{key}] {val}")
    
    print("\nSelect expense category:\n")


    while True:

        try:

            user_choice = int(input("\nSelection: ").strip())















def calculate_item_total(price: Decimal, quantity: int) -> Decimal:
    """Calculates total cost for an item and rounds to 2 decimal places."""
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if quantity < 1:
        raise ValueError("Quantity must be at least 1.")
    
    return (price * quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)








