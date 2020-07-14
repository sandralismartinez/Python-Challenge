#   PyPoll
#   Helping a small, rural town to modernize its vote counting process.
#   Given a set of data election_data.csv. The dataset is composed of three
#   columns: Voter ID, County and Candidate. Create a Python script
#   that analyses the votes and makes some calculations.

#   Dependencies
import csv
import os

#   Specify the file to load (Example 3.8)
csv_load = os.path.join("Resources", "election_data.csv")

#   Specify file to write to (Example 2.10)
txt_output = os.path.join("Analysis", "ResultsPollAnalysis.txt")

#   Variables Parameters
TotalVotes = 0
Candidates = []
CandidateVotes = {}

#   Open and read csv (Example 3.1)
with open(csv_load) as election_data:
    csvreader = csv.reader(election_data)

    #   Read header row first (Example 3.1)
    csvheader = next(csvreader)
    #   print(f"Heather: {csvheader}")

    #   Read each row
    for row in csvreader:

        #   The total number of votes calculations
        TotalVotes = TotalVotes + 1

        #   A complete list of the candidates who received votes (Third column = index 2)
        #   https://stackoverflow.com/questions/22833893/python-if-not-in-list
        CandName = row[2]

        if CandName not in Candidates:

            Candidates.append(CandName)
            #print(Candidates)

            #   The total number of votes each candidate won
            CandidateVotes[CandName] = 0
            CandidateVotes[CandName] = CandidateVotes[CandName] + 1

#   Other Parameters
Votes = []
WinningCandidate = ""
CountVotesWC = 0
    
for Name in CandidateVotes:
    #   The total number of votes each candidate won
    Votes = CandidateVotes.get("Name")
        
    #   The percentage of votes each candidate won
    Percentage = (float(Votes))/(float(TotalVotes))*100

    #   The winner of the election based on popular vote
    if (Votes > CountVotesWC):

        CountVotesWC = Votes
        WinningCandidate = Name

#   Write Results
with open(txt_output, "w") as text:

    ResultsPart1 = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {TotalVotes}\n"
        f"-------------------------\n"
    )

    ResultsPart2 = (
        f"{Name}: {Percentage:.3f}% ({Votes})\n"
    )
    ResultsPart3 = (
        f"-------------------------\n"
        f"Winner: {WinningCandidate}\n"
        f"-------------------------\n"
    )

#   Print results to Terminal        
    print(ResultsPart1)
    print(ResultsPart2)
    print(ResultsPart3)

#   Export a text file with the Results
text.write(ResultsPart1)
text.write(ResultsPart2)
text.write(ResultsPart3)
