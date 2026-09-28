import pytest
from decimal import Decimal

from month_expenses import item_total_calc, grand_total_calc, add_new_expense_or_update
@pytest.fixture
def test_categories():
    return {
        1: "Subscriptions",
        2: "Groceries",
        3: "Add new category"
    }

def test_item_total_calc_valid():

    total = item_total_calc(3, Decimal('23.50'))
    assert total == Decimal('70.50'), f'Expected "70.50", got {total}'


def test_item_total_calc_invalid_quantity():
    with pytest.raises(ValueError, match='Quantity must be at least 1.'):
        item_total_calc(0, Decimal('15.50'))


def test_item_total_calc_invalid_price():
    with pytest.raises(ValueError, match='Price cannot be negative.'):
        item_total_calc(4, Decimal('-23.50'))


def test_item_total_calc_invalid_string_price():
    with pytest.raises(ValueError, match='Price cannot be a string value'):
        item_total_calc(2, 'something')


def test_item_total_calc_invalid_string_quantity():
    with pytest.raises(ValueError, match='Quantity cannot be a string value'):
        item_total_calc('something', Decimal('23.50'))


def test_grand_total_calc():

    expenses = {
        ('Groceries', 'milk'): Decimal('35.90'),
        ('Utilities', 'electricity'): Decimal('300.00')
    }

    assert grand_total_calc(expenses) == Decimal('335.90')


def test_add_new_expense_or_update_new_item():

    expenses = {}
    is_override, old_val = add_new_expense_or_update(expenses, 'Groceries', 'eggs', Decimal('65.90'))

    assert is_override is False
    assert old_val == Decimal('0.00')
    assert expenses[('Groceries', 'eggs')] == Decimal('65.90')


def test_add_new_expense_or_update_existing_item():
    
    expenses = {('Groceries', 'bread'): Decimal('19.90')}
    is_override, old_val = add_new_expense_or_update(expenses, 'Groceries', 'bread', Decimal('23.90'))

    assert is_override is True
    assert old_val == Decimal('19.90')
    assert expenses[('Groceries', 'bread')] == Decimal('23.90')
