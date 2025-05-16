#type: ignore
import struct
import pandas as pd
import os
from pathlib import Path

def binary_to_csv(input_file, output_file):
    """
    Convert a single PRN file to CSV format.
    
    Args:
        input_file (str): Path to the input PRN file.
        output_file (str): Path to the output CSV file.
    
    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    data = []
    try:
        # Open the binary PRN file for reading
        with open(input_file, 'rb') as file:
            # Read 4 bytes at a time (one float)
            while chunk := file.read(4):
                try:
                    # Unpack the float value from the binary data
                    spectrum = struct.unpack('f', chunk)[0]
                    # Append the value to the data list
                    data.append({"Spectrum": spectrum})
                except struct.error:
                    break  # Stop if there's an unpacking error
                    
        # Create a DataFrame from the collected data
        df = pd.DataFrame(data)
        
        # Drop the first 29 rows (0-based index: 0 to 28)
        df = df.drop(index=range(0, 29))
        
        # Save the DataFrame to a CSV file
        df.to_csv(output_file, index=False)
        return True
    except Exception as e:
        print(f"Error processing {input_file}: {str(e)}")
        return False

def process_all_prn_files(input_folder, output_folder):
    """
    Process all PRN files in the input folder and save CSVs to output folder.
    
    Args:
        input_folder (str): Path to the folder containing PRN files.
        output_folder (str): Path to the folder where CSV files will be saved.
    """
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Get list of all PRN files in the input folder
    prn_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.prn')]
    
    if not prn_files:
        print(f"No PRN files found in {input_folder}")
        return
    
    # Initialize counters for successful and failed conversions
    successful = 0
    failed = 0
    
    # Process each PRN file
    for prn_file in prn_files:
        input_path = os.path.join(input_folder, prn_file)
        output_path = os.path.join(output_folder, f"{os.path.splitext(prn_file)[0]}.csv")
        
        print(f"Processing: {prn_file}")
        if binary_to_csv(input_path, output_path):
            successful += 1
        else:
            failed += 1
    
    # Print summary of the conversion process
    print("\nConversion Summary:")
    print(f"Total files processed: {len(prn_files)}")
    print(f"Successfully converted: {successful}")
    print(f"Failed conversions: {failed}")

# Example usage
input_folder = r""  # Put your input folder path here (inside the double quotes)
output_folder = r""  # Put your output folder path here (inside the double quotes)

process_all_prn_files(input_folder, output_folder)
