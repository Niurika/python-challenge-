import os
import csv

#open path/reader
csvpath = os.path.join('Resources', 'budget_data.csv')

with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

#skip header row
    csv_header = next(csvreader)
   
#store data in list
    months = []
    profit_loss = []

#add data from file to list  
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    
#total amount of months in data set
    total_months = len(months)
    net_total = sum(profit_loss)

#Average Change in profit/losses over entire period
    changes_profit_loss = []
    
    for x in range(1, len(profit_loss)):
        change = (int(profit_loss[x]) - int(profit_loss[x-1]))
        changes_profit_loss.append(change)

    average_changes = sum(changes_profit_loss)/len(changes_profit_loss)
    format_average_changes = "{:.2f}".format(average_changes)
  
#Greatest increase in profits
    greatest_increase = max(changes_profit_loss)
   
    greatest_increase_date = months[changes_profit_loss.index(greatest_increase)+1]

#Greatest decrease in profits
    greatest_decrease = min(changes_profit_loss)

    greatest_decrease_date = months[changes_profit_loss.index(greatest_decrease)+1]
    
   
#print results 
    print("Financial Analysis")

    print("-"*45)

    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${format_average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
   
   #open output file
output_file = os.path.join('Analysis', 'main_output.csv')
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    
    writer.writerow(["-"*45])
    
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${net_total}"])
    writer.writerow([f"Average Change: ${format_average_changes}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"])



        
