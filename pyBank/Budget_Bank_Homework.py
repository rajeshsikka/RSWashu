import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
input_date = []
input_rev_amt = []

# temporary variables
total_rev_amt = 0
total_no_recs = 0
rev_amt = 0
hold_rev_amt = 0
total_avg_amt = 0
total_avg_change = 0
total_diff_amt = 0
max_increase = 0
max_decrease = 0

# Code begins - Actual Processing of file
with open(pybank_csv, encoding="utf8", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        # Add input_date
        input_date.append(row[0])
        total_no_recs = total_no_recs + 1

        # Add revenue price to accululate the total revenue amount
        rev_amt = int(row[1])
        input_rev_amt.append(row[1])
        total_rev_amt = total_rev_amt + int(rev_amt) 
        
        
        #Accumulate the amounts to calculate - average price between periods
        if  total_no_recs == 1: 
            total_diff_amt = 0
            hold_rev_amt = rev_amt
            print("Revenue amt", rev_amt, "Diff Amt", total_diff_amt)
        else:
            total_diff_amt = int(rev_amt) - hold_rev_amt
            hold_rev_amt = rev_amt
            total_avg_amt = total_avg_amt + total_diff_amt
            print("Revenue amt", rev_amt, "Diff Amt", total_diff_amt)
        
        #Logic - to calculate the Greatest increase between periods
        if int(total_diff_amt) > int(max_increase):
           rev_max_date = (row[0])
           max_increase = total_diff_amt

        #Logic - to calculate the Greatest decrease between periods   
        if int(total_diff_amt) < int(max_decrease):
           rev_min_date = (row[0])
           max_decrease = total_diff_amt  

        #initialize the total difference amount between periods
        total_diff_amt = 0   

# Calulate the Average Change between periods and format it to the nearest integer
total_avg_change = total_avg_amt/41
total_avg_change = round(total_avg_change)  

# Set variable for output file
output_file = os.path.join("Resources", "Budget_final.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #Write the results to a text file
    writer.writerow(["----------------------------------"])
    writer.writerow(["      Financial Analysis          "])
    writer.writerow(["----------------------------------"])
    writer.writerow(["Total no of records:" + str(total_no_recs)])
    writer.writerow(["Total Revenue amount:" + str(total_rev_amt)])
    writer.writerow(["The Average Change:" + str(total_avg_change)])
    writer.writerow(["Greatest Increase in Profits:" + str(rev_max_date) + " " + str(max_increase)])
    writer.writerow(["Greatest Decrease in Profits:" + str(rev_min_date) + " " + str(max_decrease)])    
    
    #Display the results to the terminal 
    print("-----------------------------------")
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total no of records:", total_no_recs)
    print("Total Revenue amount:", total_rev_amt)
    print("The Average Change:", total_avg_change)
    print("Greatest Increase in Profits: " ,rev_max_date, " ", max_increase)
    print("Greatest decrease in Profits: " ,rev_min_date, " ", max_decrease)
   