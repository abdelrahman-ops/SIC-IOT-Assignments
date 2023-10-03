import csv

# Input CSV file and output CSV file
input_file = 'spotify.csv'
output_file = 'spotify_processed.csv'

# Open the input and output CSV files
with open(input_file, 'r', newline='') as csv_in, open(output_file, 'w', newline='') as csv_out:
    reader = csv.reader(csv_in)
    writer = csv.writer(csv_out)

    # Process each row in the CSV file
    for row in reader:
        # Remove commas from numeric columns (columns 6 to 13 in your case)
        for i in range(6, 14):
            row[i] = row[i].replace(',', '')

        # Write the processed row to the output file
        writer.writerow(row)
