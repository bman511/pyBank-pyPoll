import csv
#import math


months_count = 0
net_total = 0
greatest_increase = [0,"month"]
greatest_decrease = [0,"month"]
"""
with open('budget_data.csv', mode='r') as budget:
    file_data = csv.reader(budget,delimiter = ',')
    for row in file_data:
        #print(int(row[1]))
        months_count += 1


print(months_count - 1 )
"""
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
                

print(str(months_count) + "\n")
print(str(net_total)+"\n")
average_change = net_total/months_count
print(f"{round(average_change,2)}\n")
print(f"{greatest_increase[0]} - {greatest_increase[1]}\n")
print(f"{greatest_decrease[0]} - {greatest_decrease[1]}\n")
#newline='\n', optional for open(), no change if included