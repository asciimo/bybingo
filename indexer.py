import json
import csv
import argparse

def flatten_and_alphabetize(json_file, output_file):
    # Load the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Create a list of tuples (value, key) where the value comes first for sorting
    flattened_list = [(value, key) for key, values in data.items() for value in values]
    
    # Sort the list alphabetically by the value
    flattened_list.sort(key=lambda x: x[0])
    
    # Write the sorted result to a TSV (tab-separated) file
    with open(output_file, 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')  # Use tab as the delimiter
        writer.writerow(["Value", "Key"])  # Write the header
        writer.writerows(flattened_list)   # Write the rows

def main():
    # Argument parser to handle CLI input
    parser = argparse.ArgumentParser(description="Flatten and alphabetize JSON values into a tab-separated file.")
    parser.add_argument('json_file', help="Path to the input JSON file.")
    parser.add_argument('output_file', help="Path to the output TSV file.")

    args = parser.parse_args()

    # Call the function to flatten and alphabetize the JSON data
    flatten_and_alphabetize(args.json_file, args.output_file)

if __name__ == "__main__":
    main()

