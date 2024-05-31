# Modules
import csv

# Set path for file
csvpath = "PyPoll\Resources\election_data.csv"

# Variable
candidate_votes = 0
candidate_dict = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV:Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # count votes
        candidate_votes += 1

        # add to the dictionary
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1 

print(candidate_votes)
print(candidate_dict)

# create our output
output = f"""Election Results
-------------------------
Total Votes: {candidate_votes}
-------------------------\n"""

max_cand = ""
max_votes = 0

for candidate in candidate_dict.keys():
    votes = candidate_dict[candidate]
    perc = 100 * (votes / candidate_votes)

    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    # calculate max of dictionary
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output += last_line

print(output)

with(open("output_TTipp.txt", 'w') as f):
    f.write(output)
