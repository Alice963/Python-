import os
import csv
budget_data=os.path.join("Resources","budget_data.csv")
total_months=0
total_pl=0
change=0
dates=[]
profits=[]
with open(budget_data, newline ="") as csv_file:
    csvreader = csv.reader(csv_file,delimiter = ",")
    csv_header= next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value =int(first_row[1])
    for row in csvreader:
        dates.append(row[0])
        Change = int(row[1])-value
        profits.append(Change)
        value = int(row[1])
        total_months += 1
        total_pl =total_pl + int (row[1])
        greatest_increase = max(profits)
        greatest_index = profits .index (greatest_increase)
        greatest_date =dates[greatest_index]   

    greatest_decrease = min(profits)
    worst_index =profits.index(greatest_decrease)
    worst_date =dates[worst_index]

    avg_change = sum (profits)/len(profits)
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months : {str(total_months)}")
    print(f"Total:${str(total_pl)}")
    print(f"Average Change:${str(round(avg_change,2))}")
    print(f"Greatest Increase in Profits: {greatest_date}(${str(greatest_increase)})")
    print(f"GreatestDecrease in profits :{worst_date} (${str(greatest_decrease)})")
    

    line1=f"Financial Analysis \n"
    line2=f"-------------------------------\n"
    line3= f"Total Months : {(total_months)}\n"
    line4 =str(f"Total:${str(total_pl)}\n")
    line5 =str(f"Average Change:${str(round(avg_change,2))}\n")
    line6 = str(f"Greatest Increase in Profits: {greatest_date}(${str(greatest_increase)})\n")
    line7= str(f"GreatestDecrease in profits :{worst_date} (${str(greatest_decrease)})\n")
    with open("output.txt" , "w") as output_file:
        output_file.write(line1)
        output_file.write(line2)
        output_file.write(line3)
        output_file.write(line4)
        output_file.write(line5)
        output_file.write(line6)
        output_file.write(line7)