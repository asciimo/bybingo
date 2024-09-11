import json
import csv
import os
import random
import argparse

def generate_tsv_files(json_file, output_dir, file_count):
    # Load the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate the specified number of TSV files
    for file_index in range(file_count):
        output_file = os.path.join(output_dir, f'output_{file_index+1}.tsv')
        generate_single_tsv(data, output_file)

def generate_single_tsv(data, output_file):
    # Prepare the column headers (B, I, N, G, O)
    headers = ["B", "I", "N", "G", "O"]
    
    # Prepare rows: 1 header row + 5 data rows
    rows = [headers]
    
    # For each column, ensure we have unique values
    b_values = random.sample(data["B"], 5)
    i_values = random.sample(data["I"], 5)
    n_values = random.sample(data["N"], 5)
    g_values = random.sample(data["G"], 5)
    o_values = random.sample(data["O"], 5)
    
    # Place "FREE" in the 3rd column of the 4th row
    n_values[2] = "FREE"
    
    # Build the 5 rows (excluding headers)
    for row_index in range(5):
        row = [
            b_values[row_index],  # Random value from B
            i_values[row_index],  # Random value from I
            n_values[row_index],  # Random value from N (with FREE at row 3)
            g_values[row_index],  # Random value from G
            o_values[row_index],  # Random value from O
        ]
        rows.append(row)
    
    # Write the rows to a TSV file
    with open(output_file, 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        writer.writerows(rows)

def main():
    # Argument parser to handle CLI input
    parser = argparse.ArgumentParser(description="Generate tab-delimited TSV files from JSON data.")
    parser.add_argument('json_file', help="Path to the input JSON file.")
    parser.add_argument('file_count', type=int, help="Number of output TSV files to generate.")
    parser.add_argument('--output_dir', default='tsv_output', help="Directory to store the output TSV files. Default is 'tsv_output'.")

    args = parser.parse_args()

    # Call the function to generate TSV files with the provided arguments
    generate_tsv_files(args.json_file, args.output_dir, args.file_count)

if __name__ == "__main__":
    main()

