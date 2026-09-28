import pytest
from decimal import Decimal

from month_expenses import month_expenses
from file_manager import export_to_csv

def test_month_expenses(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    simulated_user_inputs = iter([
        '12400',    #income
        '2',    #get category    
        'electricity',  #get item
        '300',  #get item price
        '1',  #get item quantity
        '2'  #to stop the prompts
    ])
    monkeypatch.setattr('builtins.input', lambda prompt: next(simulated_user_inputs))

    export_data, income, expenses, balance = month_expenses()

    assert income == Decimal('12400.00'), f'Expected an income of "12400.00", got {income}.'
    assert expenses == Decimal('300.00'), f'Expected expenses costing "300.00", actual cost is {expenses}'
    assert balance == Decimal('12100.00'), f'Expected a remaining balance of "12100.00", got {balance}'
    assert export_data[('Utilities', 'electricity')] == Decimal('300.00')


def test_export_to_csv(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    expenses = {('Utilities', 'electicity'): Decimal('300.00')}
    
    export_to_csv(expenses)

    grabbed_files = list(tmp_path.glob('*.csv'))

    assert len(grabbed_files) == 1, 'At least one .csv file was expected.'
