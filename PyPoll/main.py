#PyPoll analysis

import csv

total_votes = 0
candidates = []

with(open('election_data.csv',mode="r")) as results:
    el_results = csv.reader(results,delimiter=",")
    next(el_results,None)
    for vote in el_results:
        total_votes += 1
        #check if candidate name in dictionary
          #if not, add them
          #if so, add vote for them

    #calculate percentages and add to dictionary
    #get list of vote tallies, check for max
    #Find associated candidate who is the winner      
print(total_votes)


