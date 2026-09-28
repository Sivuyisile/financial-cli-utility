import pytest
from decimal import Decimal

from expenses_cli import select_category_prompt, exps_entry_prompt

@pytest.fixture
def test_categories():
    return {
        1: "Subscriptions",
        2: "Groceries",
        3: "Add new category"
    }

def test_select_category_prompt_if_category_exists(monkeypatch, test_categories):

    monkeypatch.setattr('builtins.input', lambda prompt: "2")

    result = select_category_prompt(test_categories)

    #assert result in test_categories.values(), f'The chosen category does not exists. Expected selection from {list(test_categories.values())}, got {result}'
    assert result == "Groceries", f'Expected "Groceries", got {result}'


def test_select_category_prompt_invalid_then_valid_choice(monkeypatch, test_categories):

    simulated_user_selections = iter(['99', '1'])

    monkeypatch.setattr('builtins.input', lambda prompt: next(simulated_user_selections))

    result = select_category_prompt(test_categories)

    assert result == "Subscriptions", f'Expected "Subscriptions", got {result}'
    assert result in test_categories.values()


def test_select_category_prompt_add_new_category(monkeypatch, test_categories):

    simulated_user_selections = iter(['6', 'Gym'])

    monkeypatch.setattr('builtins.input', lambda prompt: next(simulated_user_selections))

    result = select_category_prompt(test_categories)

    assert result == 'Gym', f'Expected "Gym", got {result}'
    assert test_categories[4] == 'Gym', 'Oops! New category was NOT added to key #4 successfuly.'
    assert 'Gym' in test_categories.values(), 'Oops! New category was NOT added to key #4 successfuly.'


def test_exps_entry_prompt(monkeypatch, test_categories):

    simulated_user_inputs = iter(['2', 'milk', '23.98','-2', '2', '2'])

    monkeypatch.setattr('builtins.input', lambda pompt: next(simulated_user_inputs))

    expense_dict = {}
    amount, item, quantity, category, keep_going = exps_entry_prompt(expense_dict, test_categories)

    assert amount == Decimal('23.98'), f'Expected "23.98", got {amount}'
    assert item == 'milk', f'Expected "milk", got {item}'
    assert quantity == 2, f'Expected "2", got {quantity}'
    assert category == 'Groceries', f'Expected "Groceries", got {category}'
    assert keep_going is False
    