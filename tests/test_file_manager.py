import pytest
from decimal import Decimal

from file_manager import export_to_csv

def test_export_to_csv_empty_dict(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    export_to_csv({})

    assert list(tmp_path.glob('*.csv')) == [], 'One or more .csv files were found in the directory.'

def test_export_to_csv_writes_data(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    expenses = {
        ('Groceries', 'Milk'): Decimal('35.90'),
        ('Subscriptions', 'Netflix'): Decimal('199.90')
    }

    export_to_csv(expenses)

    grabbed_files = list(tmp_path.glob('*.csv'))
    assert len(grabbed_files) == 1, 'Only one .csv file was expected.'

    file_contents = grabbed_files[0].read_text(encoding='utf-8')

    assert 'Category,Item,Amount (R)' in file_contents
    assert 'Groceries,Milk,35.90' in file_contents
    assert 'Subscriptions,Netflix,199.90' in file_contents


def test_export_to_csv_verify_append_mode(tmp_path, monkeypatch):    #not sure if we add abo monkeypatch and tmp-path in the parenthesis here also
    monkeypatch.chdir(tmp_path)


    expense_1 = {('Groceries','Nutella'):Decimal(92.90)}
    expense_2 = {('Subscriptions', 'Amazon Prime'):Decimal(59.90)}

    export_to_csv(expense_1)
    export_to_csv(expense_2)

    selected_files = list(tmp_path.glob('*.csv'))
    assert len(selected_files) == 1, 'Only one .csv file was expected.'

    selected_file_contents = selected_files[0].read_text(encoding='utf-8')

    assert 'Groceries,Nutella,92.90' in selected_file_contents
    assert 'Subscriptions,Amazon Prime,59.90' in selected_file_contents

    header_occurrences = selected_file_contents.count('Category,Item,Amount (R)')

    assert header_occurrences == 1, f'Only one heading is expected in the sheet, found {header_occurrences}.'