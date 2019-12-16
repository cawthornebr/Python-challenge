# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/budget_data.csv')

#create variables and lists
month=[]
amount=[]
change=0
prev=0
ave=0
incamount=0
incmonth=[]
decamount=0
decmonth=[]
netamount=0

#Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row of headers
    header = next(csvreader)

    #parse out rows
    for row in csvreader:

        #add to month count
        month.append(row[0])

        #find out the change for current row
        change=int(row[1])-int(prev)

        #find greatest increase amount and month
        if change>incamount:
            incamount=change
            incmonth=row[0]

        #find greatest decrease amount and month
        if change<decamount:
            decamount=change
            decmonth=row[0]
        
        #reset prev row to current row for next loop
        prev=row[1]

        #find the average change
        if ave == 0:
            ave=int(row[1])
        else:
            ave = ave - int(row[1])
            amount.append(ave)
            ave=int(row[1])

        #add each profit and lot to total
        netamount=netamount+int(row[1])

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(month)}')
print(f'Total: ${netamount}')
print(f'Average  Change: ${round(sum(amount)*-1/len(amount),2)}')
print(f'Greatest Increase in Profits: {incmonth} ({incamount})')
print(f'Greatest Decrease in Profits: {decmonth} ({decamount})')