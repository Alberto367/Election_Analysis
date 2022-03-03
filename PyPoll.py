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

# open election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    

    # read the file object with the reader function 
    file_reader = csv.reader(election_data)

    # Print header row
    headers = next(file_reader)
    print(headers)
    


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
  






















