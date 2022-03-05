# Election Analysis

## Project Overview
The Colorado Board of Elections has given us the task to audit the election results of a local congressional elecetion.

### In this project we will:
1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources 
- Data source: election_results.csv
- Software: Python 3.7.6 Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidates results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes

- The winner of the election was:
  - Diana DeGuette, who received 73.8% of the votes and 272,892 votes.

## Overview of Election Audit
The purpose of this election audit was to determine the winner of a local congressional race for the Colorado Board of Election.

## Election-Audit Results
1. There were a total of 369,711 votes cast in this election.
```
for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
2. County Results:
    - Jefferson county had a turnout of 38,855 votes cast accounting for 10.5% of the total vote count.
    - Denver county had a turnout of 306,055 votes cast accounting for 82.8% of the total vote count.
    - Arapahoe county had a turnout of 24,801 votes cast accounting for 6.7% of the total vote count.
```
for county_name in county_votes:
        
        # 6b: Retrieve the county vote count.
        countyVotes  = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        countyVotes_percentage = float(countyVotes) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = (
                    f"{county_name}: {countyVotes_percentage:.1f}% ({countyVotes:,})\n")
```

3. Denver county had the largest voter turnout in this election.
```
if (countyVotes > county_largest_turnout_votes):
            county_largest_turnout_votes = countyVotes
            county_largest_turnout = county_name
```
4. Candidate Results:
    - Charles Casper Stockham received 85,213 votes accounting for 23.0% of the total votes cast.
    - Diana DeGette received 272,892 votes accounting for 73.8% of the total votes cast.
    - Raymon Anthony Doane received 11,606 votes accounting for 3.1% of the total votes cast.

```
for candidate_name in candidate_votes:
    #Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```

5. Diana DeGette won the election with a total of 272,892 votes received giving her 73.8% of the total votes cast.
```
if  (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage
```


## Election-Audit Summary
1. This script can be modified to to include UDFs (User-Defined Functions) so other users can referance our code with ease and apply it to other election audits.

2. We could also have better modularity by sperating our functions to make it more readable and reuse friendly, such as sperating the code for counties and the code for candidates. This will make it easiler to reuse certain aspect of our code in other elections.