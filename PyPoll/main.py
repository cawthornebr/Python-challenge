# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/election_data.csv')

#create variables, lists, and dictionarys 
totalvotes=0
blerb={}
#Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row of headers
    header = next(csvreader)
    
    for row in csvreader:

        #for each row add one to the total votes
        totalvotes=totalvotes+1

print(totalvotes)