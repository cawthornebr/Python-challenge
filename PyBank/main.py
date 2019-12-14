# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/budget_data.csv')

#create a list for months
month=[]

#Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #splits file by row
    for row in csvreader:

        #add each month to the month list
        month.append(row[0])

#display the number of months minus the header
print(len(month)-1)