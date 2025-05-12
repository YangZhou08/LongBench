import json 
import csv 

import argparse 

parser = argparse.ArgumentParser() 
parser.add_argument("--local_dir", type = str) 

args = parser.parse_args() 

with open(args.local_dir, "r") as file: 
    data = json.load(file) 

# Output to CSV format
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "0-4k", "4-8k", "8k+"])  # header
    
    for name, values in data.items(): 
        # print("{},{},{},{}".format(name,
        #         values.get("0-4k", ""),
        #         values.get("4-8k", ""),
        #         values.get("8k+", ""))) 
        print("{},{},{}".format(
                values.get("0-4k", ""), 
                values.get("4-8k", ""), 
                values.get("8k+", ""))) 

print("CSV file 'output.csv' has been written.") 
