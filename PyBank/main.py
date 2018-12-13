#PyBank analysis
import csv

#define all variables for tallies and calcs
months_count = 0
net_total = 0
greatest_increase = [0,"month"]
greatest_decrease = [0,"month"]
changeOverSum = 0
changeArr = [0,0]

with open('budget_data.csv', mode='r') as budget:
    file_data = csv.reader(budget,delimiter = ',')
    #skip headers
    next(file_data,None)
    for row in file_data:
        #each row is a month, so increment month variable
        months_count += 1
        #add the month's profit/loss to the total
        net_total += int(row[1])
        #check if month's profit is the greatest thus far. If so, assign to variable.
        if(int(row[1]) > greatest_increase[0]):
            greatest_increase = [int(row[1]),row[0]]
        #check if month's loss is greatest, if so assign to variable
        elif(int(row[1]) < greatest_decrease[0]):
            greatest_decrease = [int(row[1]),row[0]]
        #this if/else will accrue the difference between months by subtracting last month from current month
        #the first month is a unique case, so assign it's value to index 1 of the array, then continue
        if(months_count == 1):
            changeArr[1] = row[1]
            continue
        #rearrange the array, add last month to index 0 and this month to index 1, then subtract the two and
        #store in accumulated change variable
        else:
            changeArr[0] = changeArr[1]
            changeArr[1] = row[1]
            changeOverSum += int(changeArr[1])-int(changeArr[0])
    #define function that prints and writes-to-file a string passed to it
    def printWrite(theString,fileName):
        print(theString)
        fileName.write(theString)
    #define output file
    theFileName = "budgetResults.txt"
    #build array of strings to print/write 
    resultsArr = ["\nFinancial Analysis\n----------------\n",
                f"Total Months: {months_count}\n",
                f"Total: ${net_total}\n",
                f"Average Change: ${round(changeOverSum/months_count-1,2)}\n",
                f"Greatest Increase in Profits: {greatest_increase[1]} (${greatest_increase[0]})\n",
                f"Greatest Decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[0]})\n",
                "-----------------" ]
    #create the output file, and call the printWrite function for each string in the array
    with open(theFileName,"w") as output:
        for string in resultsArr:
            printWrite(string,output)
            
