# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/budget_data.csv')

#create a list for months and net profit/loss
month=[]

#total amout set as 0
netamount=0

#average change as list
ave=[]

#Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row of headers
    header = next(csvreader)

    #parse out rows
    for row in csvreader:
        month.append(row[0])
        netamount=netamount+int(row[1])

    print(len(month))
    print(netamount)
