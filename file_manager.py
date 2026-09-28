#newn notes
import os
 
import csv
from datetime import datetime


#initially, for the below argument, I wanted to say 'month_expense_dict' but then I though of when I use this for a yearly to whatever period periodical expense tracker that exports to .csv
def export_to_csv(expenses_dict):

    if not expenses_dict:
        print("Woops! No expenses to export.")
        return

    this_month = datetime.now().strftime('%B %Y')
    csv_file_name = f'expense_tracker_{this_month.replace(" ", "_")}.csv'

    #new notes
    file_exists = os.path.exists(csv_file_name)

    with open(csv_file_name, mode='a', newline='') as file_to_output:

        csv_writer = csv.writer(file_to_output, delimiter=',')

        if not file_exists: #new notes
            csv_writer.writerow(['Category', 'Item', 'Amount (R)']) #headings first

        for (category, item), amount in expenses_dict.items():
                csv_writer.writerow([category, item.title(), f'{amount:.2f}'])

    print(f'Success: Expenses exported to {csv_file_name}')