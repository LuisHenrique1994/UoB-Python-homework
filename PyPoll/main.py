import csv


# Initialising variables
tot_votes = 0
candidates_with_votes = set()
percentages_votes = {}
votes_for_each = {}
winner = None


# Opening csv file
with open('Resources/election_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for vote in reader:
        tot_votes += 1
        candidates_with_votes.add(vote['Candidate'])
        votes_for_each[vote['Candidate']] = votes_for_each.get(vote['Candidate'], 0) + 1
    
    max_votes = max(votes_for_each.values())
    for candidate in candidates_with_votes:
        percentages_votes[candidate] = votes_for_each[candidate] / tot_votes * 100
        if votes_for_each[candidate] == max_votes: winner = candidate


with open('analysis/results.txt', 'w') as results_file:
    print(f"Election Results")
    results_file.write(f"Election Results\n")
    print("-" * 40)
    results_file.write("-" * 40 + "\n")
    print(f"Total Votes: {tot_votes}")
    results_file.write(f"Total Votes: {tot_votes}\n")
    print("-" * 40)
    results_file.write("-" * 40 + "\n")
    
    for candidate in sorted(candidates_with_votes):
        print(f"{candidate}: {percentages_votes[candidate]:.3f}% ({votes_for_each[candidate]})")
        results_file.write(f"{candidate}: {percentages_votes[candidate]:.3f}% ({votes_for_each[candidate]})\n")
    print("-" * 40)
    results_file.write("-" * 40 + "\n")
    print(f"Winner: {winner}")
    results_file.write(f"Winner: {winner}\n")
    print("-" * 40)
    results_file.write("-" * 40 + "\n")