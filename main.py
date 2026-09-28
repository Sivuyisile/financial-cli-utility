from month_expenses import month_expenses
from file_manager import export_to_csv


if __name__ == '__main__':
    export_data, income, expenses, balance = month_expenses()
    export_to_csv(export_data)