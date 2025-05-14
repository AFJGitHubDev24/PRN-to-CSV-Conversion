## PRN-to-CSV-Conversion using Python 📜 -> 💻
This script is a handy tool for converting binary PRN files — specifically ones containing float data—into clean, readable CSV files. It reads each PRN file one float (4 bytes) at a time, extracts the data, skips the first 29 records (likely some kind of header or unwanted preamble), and then writes the rest to a CSV format. It’s built to handle batches too: you just point it at a folder of PRN files, and it churns out the corresponding CSVs into a specified output folder. It even keeps score, telling you how many conversions succeeded or failed—so you can spot trouble without guessing.

# Function to convert binary PRN to CSV:
  1. Opens the PRN file in binary mode.
  2. Reads 4 bytes at a time (size of a float).
  3. Unpacks the bytes into a floating-point number and stores them in a list
  4. Converts extracted float values into a Pandas DataFrame.
  5. Drops the first 29 rows (assumed to be unnecessary header data).
  6. Writes the cleaned data to a CSV file.

# Function to process all PRN files:
1. Create an output folder to ensure that the same thing exists before writing files.
2. Lists and filters the input PRN files.
3. Iteration over each PRN file and generate corresponding CSV file names for output.
4. Calls the function to convert binary PRNs to CSVs
5. Two counters – successful and failed, for tracking the number of successful and failed conversions.
6. Print the summary of the conversion process.

# Example usage:
1. Specifies the input and output folders (for example, 'inputprnswavecalibration' for input PRN files related to wave calibration, and 'outputcsvswavecalibration' to store the resultant CSV files related to wave calibration.
2. Calls the function to process all PRN files in the input folder.

# Note:
This script was created with a team of Junior Data Science Developer Interns from Ocean Oasis, a Norwegian-Spanish based water desalination company, which uses wave power of the ocean to produce freshwater.
