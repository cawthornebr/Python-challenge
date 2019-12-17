# Dependencies
import os
import csv

#define path of csv file
csvpath = os.path.join('Resources/budget_data.csv')

# Specify the file to write to
output_path = os.path.join("Results.txt")

#create variables and lists needed
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

    #loop through csv
    for row in csvreader:

        #add to month count
        month.append(row[0])

        #find out the change for current row
        change=int(row[1])-int(prev)

        #reset prev row to current row for next loop
        prev=row[1]

        #add each profit and lot to total
        netamount+=int(row[1])

        #find greatest increase amount and month
        if change>incamount:
            incamount=change
            incmonth=row[0]

        #find greatest decrease amount and month
        if change<decamount:
            decamount=change
            decmonth=row[0]

        #find the average change
        if ave == 0:
            ave=int(row[1])
        else:
            ave -= int(row[1])
            amount.append(ave)
            ave=int(row[1])

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    txtwriter = csv.writer(txtfile, delimiter=',', quoting=csv.QUOTE_NONE, quotechar='')

    #print final text and write to file
    print(f"Financial Analysis\n----------------------------\nTotal Months: {len(month)}\nTotal: ${netamount}")
    print(f"Average  Change: ${round(sum(amount)*-1/len(amount),2)}\nGreatest Increase in Profits: {incmonth} (${incamount})")
    print(f"Greatest Decrease in Profits: {decmonth} (${decamount})")
    txtwriter.writerow(["Financial Analysis"])
    txtwriter.writerow(["-------------------------"])
    txtwriter.writerow(["Total Months: "+str(len(month))])
    txtwriter.writerow(["Total: $"+str(netamount)])
    txtwriter.writerow(["Average  Change: $"+str(round(sum(amount)*-1/len(amount),2))])
    txtwriter.writerow(["Greatest Increase in Profits: "+incmonth+" ($"+str(incamount)+")"])
    txtwriter.writerow(["Greatest Decrease in Profits: "+decmonth+" ($"+str(decamount)+")"])