import csv


# Opening csv file and declaring variables
csvpath = 'Resources/budget_data.csv'
with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    tot_months = 0
    net_tot = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]
    last_value = 0
    changes = []
    
    # Iterating through rows
    for date, value in reader:
        if reader.line_num == 1: continue
        value = int(value)
        if reader.line_num == 2:
            tot_months += 1
            net_tot += value
            last_value = value
            greatest_increase[1] = value
            greatest_decrease[1] = value
            continue
        # Adding the result of the substraction to the changes list to calculate the average
        changes.append(value - last_value)
        
        tot_months += 1
        net_tot += value
        if greatest_increase[1] < value - last_value:
            greatest_increase[1] = value - last_value
            greatest_increase[0] = date
        
        if greatest_decrease[1] > value - last_value:
            greatest_decrease[1] = value - last_value
            greatest_decrease[0] = date
        
        last_value = value


# Printing (writing) results to the txt file
with open("./analysis/results.txt", "w") as results:
    results.write("Financial Analysis\n")
    results.write("-"*40 + '\n')
    results.write(f"Total months: {tot_months}\n")
    results.write(f"Total: ${net_tot}\n")
    results.write(f"Average Change: ${sum(changes)/(tot_months - 1):.2f}\n")
    results.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    results.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    
# Printing results to the console
    print("Financial Analysis\n")
    print("-"*40 + '\n')
    print(f"Total months: {tot_months}\n")
    print(f"Total: ${net_tot}\n")
    print(f"Average Change: ${sum(changes)/(tot_months - 1):.2f}\n")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")