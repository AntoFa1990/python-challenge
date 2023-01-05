# Import modules
import os, csv
from pathlib import Path 

# Assign file location within the pathlib library
csv_file_path = Path("Resources", "election_data.csv")

# Declare Variables 
total_votes = 0 
candidate_names = []
candidate_votes = {}
votes = 0
winner = ""
winner_vote = 0


# Open csv in default read mode with context manager
with open(csv_file_path) as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # Declare variable for candidates name 
        candidate_name = row[2]
        # If the candidates name is not in the name list add it and set initial vote count to zero
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votes [candidate_name]= 0
        #add candidate vote
        candidate_votes [candidate_name] += 1


output_file = Path("analysis", "Election_Results_Summary.txt")

with open(output_file,"w") as file:
    election_output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------

"""
    print (election_output)
    file.write(election_output)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentage = votes/total_votes*100

        if votes > winner_vote:
            winner_vote = votes
            winner = candidate

        candidate_results = f"{candidate}: {percentage:.2f}% ({votes})\n"

        print (candidate_results)
        file.write(candidate_results)
    
    winner_output = f"""
-------------------------
Winner: {winner}
-------------------------


    """
    print (winner_output)
    file.write(winner_output)
