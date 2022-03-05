# The data we need to retrieve
# 1. total number of votes 
# 2. A complete list of canidates thta recived votes
# 3. The percentage of votes each canidate won
# 4. The total number of votes each canidayte won
# 5. The winner of the election based on popular vote

# When you know the path
# Assign a variable for the file to load and the path
##file_to_load = 'Resources/election_results.csv'

# Open the elecetion results and read the file
##with open(file_to_load) as election_data:

    # To do: perform analysis
  ##  print(election_data)

# When you don't know the path
#import modules
import csv
import os
# Assign a variable to load fiel from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to load a file a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter. Always before the code
total_votes = 0

# Candidate options 
candidate_options = []
# Declare empty dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open election results and read the file
with open(file_to_load) as election_data:
    # read the file object with the reader function 
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)
    

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        #Print the candidate name for each row
        candidate_name = row[2]

        # Add if statement to add candidates
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begion tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")

    print(election_results, end="")
    # Save the final vote count to the text file.       
    txt_file.write(election_results)

    # Determine percentage of votes for each candidate
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        #2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #3 Calculate the percentage of votes
        vote_percentages = float(votes)/float(total_votes) * 100

        # Print out each candidate name, vote count, and percentage of votes
        candidate_results = (
            f"{candidate_name}: {vote_percentages:.1f}% ({votes:,})\n")
        
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

    ## Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentages > winning_percentage):
            # if true then set winning_count = to votes and winning_percentages = to vote_percentages
            winning_count = votes
            winning_percentage = vote_percentages
            # and set winning_candidate = to candidate_name
            winning_candidate = candidate_name

    # Print winning results in terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percenatge: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)











