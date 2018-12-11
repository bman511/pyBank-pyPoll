#PyBank analysis
import csv
#import math
#edit

months_count = 0
net_total = 0
greatest_increase = [0,"month"]
greatest_decrease = [0,"month"]
changeOverSum = 0
changeArr = [0,0]

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
        if(months_count == 1):
            changeArr[1] = row[1]
            continue
        else:
            changeArr[0] = changeArr[1]
            changeArr[1] = row[1]
            #print(changeArr)
            changeOverSum += int(changeArr[1])-int(changeArr[0])
            #print(changeOverSum)
    def printWrite(theString,fileName):
        #print(theString)
        fileName.write(theString)
    
    theFileName = "budgetResults.txt"
     
    resultsArr = ["\nFinancial Analysis\n----------------\n",
                f"Total Months: {months_count}\n",
                f"Total: ${net_total}\n",
                #f"Average Change: ${round(net_total/months_count,2)}\n",
                f"Average Change: ${round(changeOverSum/months_count-1,2)}\n",
                f"Greatest Increase in Profits: {greatest_increase[1]} (${greatest_increase[0]})\n",
                f"Greatest Decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[0]})\n",
                "-----------------" ]
    with open(theFileName,"w") as output:
        for string in resultsArr:
            printWrite(string,output)
            

#changeOverSum = 0
#changeArr = [0,0]
#changeArr[0] = changeArray[1]
#changeArr[1] = row[1]
#changeOverSum += changeArr[1]-changeArr[0]
