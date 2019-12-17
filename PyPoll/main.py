# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/election_data.csv')

votes={}

#create variables, lists, and dictionarys 
totalvotes=0

#Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row of headers
    header = next(csvreader)
    
    for row in csvreader:
        vote=row[2]
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1 
        #for each row add one to the total votes
        totalvotes+=1

max=0
maxname=""

print(f"""Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------""")
for vote, num in votes.items():
    print(f'{vote}: {round(float(num)/totalvotes*100,3)}00% {str(num)}')
    if num>max:
        max=num
        maxname=vote
print(f"""-------------------------
Winner: {maxname}
-------------------------""")