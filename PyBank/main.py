from calendar import c
import csv
import os


csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as budget_file:
    budget_data = csv.reader(budget_file)
    tot_months = len(list(budget_data)) - 1
    
    for row in budget_data:
        print(row)
# print()

