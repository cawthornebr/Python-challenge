# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/election_data.csv')

# Specify the file to write to
output_path = os.path.join("Results.txt")

#create variables, dictionaries, and lists needed
totalvotes=0
votes={}
max=0
maxname=""

#Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row of headers
    header = next(csvreader)
    
    #loop through csv
    for row in csvreader:

        #assign variable vote to the name of the person in current row
        vote=row[2]

        #if the name is in the dictionary, then add one. if it's not in dictionary, value for that name is 1
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1 
        
        #for each row add one to the total vote count
        totalvotes+=1

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    txtwriter = csv.writer(txtfile, delimiter=',', quoting=csv.QUOTE_NONE, quotechar='')

    #print first set of text and write to txt file
    #--------------------
    print(f"Election Results\n-------------------------\nTotal Votes: {totalvotes}\n-------------------------")
    txtwriter.writerow(["Election Results"])
    txtwriter.writerow(["-------------------------"])
    txtwriter.writerow(["Total Votes: "+str(totalvotes)])
    txtwriter.writerow(["-------------------------"])
    #--------------------

    #loop through dictionary
    for vote, num in votes.items():

        #print name, percent of total votes, and vote count for each name and write to txt file
        print(f'{vote}: {round(float(num)/totalvotes*100,3)}00% ({str(num)})')
        txtwriter.writerow([vote+": "+str(round(float(num)/totalvotes*100,3))+"00% ("+str(num)+")"])

        #find max value and max value name
        if num>max:
            max=num
            maxname=vote

    #print the last section of text and write to txt file
    print(f"-------------------------\nWinner: {maxname}\n-------------------------")
    txtwriter.writerow(["-------------------------"])
    txtwriter.writerow(["Winner: "+maxname])
    txtwriter.writerow(["-------------------------"])