#PyPoll analysis
import os
import csv

total_votes = 0
candidates = {}

with open('election_data.csv',mode="r") as results:
    el_results = csv.reader(results,delimiter=",")
    #skip headers
    next(el_results,None)
    for vote in el_results:
        #tally total votes
        total_votes += 1
        #check if candidate has already been added to dictionary
        if candidates.get(vote[2]):
            #assign current candidates name to variable
            curCan = vote[2] 
            #increment a vote for that candidate
            totalVote = candidates[curCan] + 1
            #assign candidates new vote total in dictionary
            candidates[curCan] = totalVote
        else: #if candidate is not present, add them and give them one vote
          candidates[vote[2]] = 1  
     #define function to print and write string               
    def printWrite(theString,fileName):
        print(theString)
        fileName.write(theString)
    
    theFileName = "electionResults.txt"
    winnerNum = 0
    outDivide = "\n-------------------------\n"
    outTitle = "\nElection Results" + "\n" + outDivide
    outTotalVotes = f"Total Votes: {total_votes}" + outDivide
    #create output file and print/write above variables
    with open(theFileName,"w") as output:
        printWrite(outTitle,output)
        printWrite(outTotalVotes,output)
        #iterate through dictionary and print candidate and votes       
        for cand,voteTotal in candidates.items():
            printWrite(f"{cand}: {str(round((voteTotal/total_votes)*100,3))}% ({voteTotal})\n",output)
            #assign highest votes to corresponding candidate
            if voteTotal > winnerNum:
                winnerNum = voteTotal
                winnerName = cand
            
        printWrite(outDivide,output)
        printWrite(f"Winner: {winnerName}",output)
        printWrite(outDivide,output)
        



