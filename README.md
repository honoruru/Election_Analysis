# Election_Analysis

## Project Overview
The project involved developing a Python script to deliver a report to the Colorado Board of Elections for a U.S. Congressional District election.  The report must include: 
 1. The total number of votes cast
 2. A complete list of candidates who received votes
 3. The percentage of votes each candidate won
 4. The total number of votes each candidate won
 5. The winner of the election based on populare vote.

The report will be used to certify the results of the election. 

## Resources
 1. Data source:  election_results.csv
 2. Software: Python 3.7, Visual Studio Code, 1.5.7 

## Summary
The analysis of the election results show that:
1.  There were 369,711 votes cast in the election.
2.  The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthong Doand
3.  The election results were:
    - Charles Casper Stockham received 23.0% of the vote and 82,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthong Doane received 3.1% of the vote and 11,606 number of votes.
4.  The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.
    
## Challenge Overview
Business Proposal

The script developed to certify the results of the current U.S. Congressional District election can be readily applied to other elections. This includes municipal, Senatorial, and even Presidential elections. 

The process for producing the report would not require staff with computer coding skills.  The requirements would be limited to:
-	a “CSV” file for every vote cast that includes:
    - Ballot unique identifier (e.g., Ballot ID)
    - Candidate voted for 
    - Voter segments, if any (e.g., county, precinct, ward)

-	a secured computer environment to ensure that the script is not tampered with, except as authorized by election officials

The “chain of custody” of the “CSV” file produced by the Central Office from production to the secured computer environment is critical in ensuring the integrity of the election and satisfying regulatory requirements. Once secured in the environment, elections staff would begin the report production process. 

A portal would be accessible to only to authorized elections staff to input simple information (name and folder location of “CVS” file) to begin the report generation process.  Vote counts of 500,000 or less have been demonstrated to take less than a second to produce. This portal would be developed by our firm. 

NOTE:  The portal described would be an election staff user interface with the election script.  This would control the input to only required and all required fields.  If practicable, input would be by drop-down menu.

## Challenge Summary
As montioned, the script could be modified to accomodate different types of elections from Congressional to "Name that Highway.

### Senatorial Election

In this example, little modification is required as it is assumed that the Senatorial districts are the same counties used in the Congressional election.  It is also assumed that these elections produce only one winner.

In this election, the election staff would simply input the exact name and folder location of “CVS” file.

### Any Election that does not use County as the Voter Segment

The code would be modified to handle any election with voters segmented into groups other than “county” (e.g., precinct, ward).  This would be accomplished by defining variable for the name of the segment.  Throughout the script, the variable would be inserted wherever “county” appeared.

In these elections, the election staff would also input the exact name of the segment, in addition to the exact name and folder location of “CVS” file.

This would likely be the standard model of the script. 

### An Election with Two Winners

For an election with multiple winners such as a primary where each party has a winner, the code would be modified to include the following modifications:

-	party_option list
-	filter to exclude votes where candidate and party were mismatched (these votes could be tallied and displayed)
-	selection of candidate with most votes for each party

The results for each party would be displayed separately to show the candidate with the most votes from each party.  



