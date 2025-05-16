# PRN to CSV Conversion 📜 -> 💻
This repository offers a streamlined solution for converting `.prn` (Print) files into `.csv` (Comma-Separated Values) format using Python. Designed for data analysts and developers, this tool simplifies the transformation of fixed-width text files into structured CSV files for easier data manipulation and analysis.

## 🚀 Features

* **Flexible Parsing**: Handles fixed-width `.prn` files with customizable field widths.
* **Automated Conversion**: Processes multiple `.prn` files in batch mode.
* **Error Handling**: Includes robust error checking and logging mechanisms.
* **User-Friendly Interface**: Simple command-line interface for ease of use.

## 🛠️ Technologies Used

* **Python 3.8+**: Core programming language for scripting and automation.
* **Pandas**: Data manipulation and analysis library for handling tabular data.
* **NumPy**: Supports numerical operations and array handling.
* **argparse**: Facilitates command-line argument parsing.

## 📦 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AFJGitHubDev24/PRN-to-CSV-Conversion.git
   cd PRN-to-CSV-Conversion
   ```



2. **Create a Virtual Environment (Optional but Recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**:
   
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Usage

```bash
python prn_to_csv_converter.py --input_file path/to/input.prn --output_file path/to/output.csv
```



### Command-Line Arguments:
* `--input_file`: Path to the input `.prn` file.
* `--output_file`: Desired path for the output `.csv` file.
* `--field_widths`: (Optional) Comma-separated list of field widths.
* `--delimiter`: (Optional) Delimiter for the output CSV file (default is comma).

### Example:
```bash
python prn_to_csv_converter.py --input_file data/sample.prn --output_file data/output.csv --field_widths 10,15,20 --delimiter ","
```



## 📁 Project Structure
```
PRN-to-CSV-Conversion/
├── data/
│   ├── sample.prn
│   └── output.csv
├── prntocsv.py
├── requirements.txt
└── README.md
```



## 🧪 Testing

Note: Direct running of the Python code is enough!

To run the test suite:

```bash
python -m unittest discover tests
```
Ensure that all tests pass to validate the functionality of the converter.

## 📄 License
This project is licensed under the [GNU General Public License v3.0](LICENSE).

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📬 Contact
For questions or suggestions, feel free to open an issue or contact [AFJGitHubDev24](https://github.com/AFJGitHubDev24).

## Note: 
The sample PRNs are unable to displayed as there is no direct option to open a PRN file due to it's binary-coded format!
