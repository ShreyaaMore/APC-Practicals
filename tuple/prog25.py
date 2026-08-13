# Store runs scored in 10 matches and calculate:
# •	Total runs 
# •	Highest score 
# •	Lowest score 
# •	Average score 

runs_scored = (76,45,53,88,57,68,41,54,63,71)

print(f"Total runs: {sum(runs_scored)}")
print(f"Highest Runs: {max(runs_scored)}")
print(f"Lowest Runs: {min(runs_scored)}")
print(f"Average Runs: {sum(runs_scored)/len(runs_scored)}")
