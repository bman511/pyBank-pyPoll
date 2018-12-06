#PyPoll analysis
import os
import csv

total_votes = 0
candidates = {}

with(open('election_dataTest.csv',mode="r")) as results:
    el_results = csv.reader(results,delimiter=",")
    #next(el_results,None)
    for vote in el_results:
        total_votes += 1
        if candidates.get(vote[2]):
            #assign current candidates name to variable
            curCan = vote[2] 
            #increment a vote for that candidate
            totalVote = candidates[curCan] + 1
            #assign candidates new vote total in dictionary
            candidates[curCan] = totalVote
        else:
          candidates[vote[2]] = 1  
          #if not, add them
          #if so, add vote for them
        
    def printWrite(theString,fileName):
        print(theString)
        fileName.write(theString)
    
    theFileName = "electionResults.txt"
    winnerNum = 0
    #winnerName = ""
    outDivide = "\n-------------------------\n"
    outTitle = "\nElection Results" + "\n" + outDivide
    outTotalVotes = f"Total Votes: {total_votes}" + outDivide
    
    with open(theFileName,"w") as output:
        printWrite(outTitle,output)
        printWrite(outTotalVotes,output)
       
    #print("\nElection Results" + "\n" + "-------------------------")
    #print(f"Total Votes: {total_votes}")  
    #print("-------------------------")
        for cand,voteTotal in candidates.items():
            printWrite(f"{cand}: {str(round((voteTotal/total_votes)*100,3))}% ({voteTotal})\n",output)
            if voteTotal > winnerNum:
                winnerNum = voteTotal
                winnerName = cand
            
        printWrite(outDivide,output)
        #print("-------------------------")
        printWrite(f"Winner: {winnerName}",output)
        printWrite(outDivide,output)
        #print("-------------------------\n")



