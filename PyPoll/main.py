import os 
import csv 

csvpath = os.path.join('Resources', 'election_data.csv')

with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    csv_header = next(csvreader)

    candidates_list = []

    for row in csvreader:
        candidates_list.append(row[2])

#list of candidates
    unique_candidates = []
    for candidate in candidates_list:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    
    candidate_count = len(unique_candidates)
    
#votes/percent per candidate
    votes = []
    percent = []
    
    for i in range (0, candidate_count):
        name = unique_candidates[i]
        votes.append(candidates_list.count(name))
        percentage_calc = (votes[i]/len(candidates_list))
        percent.append(percentage_calc)
        
    winner_index = votes.index(max(votes)) 
    
    total_num_votes = len(candidates_list)

    print("Election Resultus")

    print("-"*45)

    print(f"Total Votes: {total_num_votes}")

    print("-"*45)

    for i in range (0, candidate_count):
        print(f"{unique_candidates[i]}: {percent[i]:.3%} ({votes[i]})")

    print("-"*45)

    print(f"Winner: {unique_candidates[winner_index]}")

    print("-"*45)

output_file = os.path.join('Analysis', 'main_output.csv')
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Election Resultus"])
    
    writer.writerow(["-"*45])
    
    writer.writerow([f"Total Votes: {total_num_votes}"])
    
    writer.writerow(["-"*45])
    
    for i in range (0, candidate_count):
        writer.writerow([f"{unique_candidates[i]}: {percent[i]:.3%} ({votes[i]})"])
    
    writer.writerow(["-"*45])
    
    writer.writerow([f"Winner: {unique_candidates[winner_index]}"])

    writer.writerow(["-"*45])


