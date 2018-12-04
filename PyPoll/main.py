#PyPoll analysis

import csv

total_votes = 0
candidates = {}

with(open('election_dataTest.csv',mode="r")) as results:
    el_results = csv.reader(results,delimiter=",")
    #next(el_results,None)
    for vote in el_results:
        total_votes += 1
        if candidates.get(vote[2]):
            curCan = vote[2]
            totalVote = candidates[curCan] + 1
            candidates[curCan] = totalVote
        else:
          candidates[vote[2]] = 1  
          #if not, add them
          #if so, add vote for them
    
    #calculate percentages and add to dictionary
    #get list of vote tallies, check for max
    #Find associated candidate who is the winner
    
for cand,voteTotal in candidates.items():
    print(cand + " " + str(voteTotal) + "\n")
print(total_votes)

#print(len(candidates))

