import os
import csv

csvpath = os.path.join("PyBank/Resources/budget_data.csv") 

with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    