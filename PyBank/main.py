#PyBank analysis
import csv
#import math
#edit

months_count = 0
net_total = 0
greatest_increase = [0,"month"]
greatest_decrease = [0,"month"]

with open('budget_data.csv', mode='r') as budget:
    file_data = csv.reader(budget,delimiter = ',')
    next(file_data,None)
    for row in file_data:
        months_count += 1
        net_total += int(row[1])
        if(int(row[1]) > greatest_increase[0]):
            greatest_increase = [int(row[1]),row[0]]
        elif(int(row[1]) < greatest_decrease[0]):
            greatest_decrease = [int(row[1]),row[0]]
                
    def printWrite(theString,fileName):
        print(theString)
        fileName.write(theString)
    
    theFileName = "budgetResults.txt"
     
    resultsArr = ["\nFinancial Analysis\n----------------\n",
                f"Total Months: {months_count}\n",
                f"Total: ${net_total}\n",
                f"Average Change: ${round(net_total/months_count,2)}\n",
                f"Greatest Increase in Profits: {greatest_increase[1]} (${greatest_increase[0]})\n",
                f"Greatest Decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[0]})\n",
                "-----------------" ]
    with open(theFileName,"w") as output:
        for string in resultsArr:
            printWrite(string,output)
            
