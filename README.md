## PRN-to-CSV-Conversion using Python 📜 -> 💻
Used Python libraries such as struct, Pandas, os and pathlib for converting binary encoded PRN files into CSV files containing numerical values.

# Function to convert binary PRN to CSV:
  Opens the PRN file in binary mode.
  Reads 4 bytes at a time (size of a float).
  Unpacks the bytes into a floating-point number and stores them in a list
  Converts extracted float values into a Pandas DataFrame.
  Drops the first 29 rows (assumed to be unnecessary header data).
  Writes the cleaned data to a CSV file.

# Function to process all PRN files:
  Create an output folder to ensure that the same thing exists before writing files.
  Lists and filters the input PRN files.
  Iteration over each PRN file and generate corresponding CSV file names for output.
  Calls the function to convert binary PRNs to CSVs
  Two counters – successful and failed, for tracking the number of successful and failed conversions.
  Print the summary of the conversion process.

# Example usage:
Specifies the input and output folders
Calls the function to process all PRN files in the input folder.![image](https://github.com/user-attachments/assets/a1a51e33-b055-404c-9e6b-3bfed69a7dbc)
