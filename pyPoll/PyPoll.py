import os
import csv
from collections import Counter
from collections import defaultdict

# place where the csv file resides
pypoll_csv = os.path.join("Resources", "election_data.csv")

# Define a default dict to accumulate the total for each Candidate
d = defaultdict(int)

# Define variables for calculations
tot_no_votes = 0
percent = 0

# Open the csv file and read it using csv.dictreader
with open(pypoll_csv, encoding="utf8", newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    #csv_header = next(csvreader) 
  
    for line in csvreader:
       tot_no_votes = tot_no_votes + 1
       d[line['Candidate']] += 1
           
    print(d)
         
    #Display the results to the terminal 
    print("-----------------------------------")
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", tot_no_votes)
    print("-----------------------------------")
    for Candidate, Votes in d.items():
        percent = (Votes/tot_no_votes) * 100
        percent = round(percent,3)
        print(Candidate,":",percent,"%","[",Votes,"]")
    print("-----------------------------------")
    winner = max(d.keys(), key=(lambda k: d[k]))
    print("Winner:", winner) 
    print("-----------------------------------")  

# Set variable for output file
output_file = os.path.join("Resources", "election_final.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #Write the results to a text file
    writer.writerow(["----------------------------------"])
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------------"])
    writer.writerow(["Total Votes:" + str(tot_no_votes)])
    writer.writerow(["----------------------------------"])
    for Candidate, Votes in d.items():
        percent = (Votes/tot_no_votes) * 100
        percent = round(percent,3)
        #writer.writerow([Candidate,":",percent,"%","[",Votes,"]"])
        writer.writerow([str(Candidate) + ":" + str(percent) + " " + "%" + " " + "[" + str(Votes) + "]"])
    writer.writerow(["----------------------------------"])
    writer.writerow(["Winner:" + str(winner)])
    writer.writerow(["----------------------------------"])