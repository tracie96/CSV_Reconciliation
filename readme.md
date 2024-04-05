# CSV Reconciliation Challenge Documentation.

## Overview

This tool provides a command-line interface (CLI) for running the reconciliation process and generating reconciliation reports. It supports features such as parsing CSV files, identifying missing records, comparing fields, and generating reconciliation reports in CSV format.

## Features i added

- **Parsing CSV Files:** Parse CSV files and convert them into pandas DataFrames for further processing.
- **Identifying Missing Records:** Identify records that are missing in either the source or target CSV file.
- **Comparing Fields:** Compare specified fields between the source and target CSV files to identify discrepancies.
- **Generating Reconciliation Reports:** Generate reconciliation reports in CSV format, detailing missing records and field discrepancies.
- **Customizable Column Comparison:** Allow users to configure which columns to compare during reconciliation, providing flexibility and customization options.

## Usage

### Running the Reconciliation Script:

1. **Setup:**
   - Install the required dependencies by running:
     ```
     pip install pandas tabulate
     ```

2. **Prepare CSV Files:**
   - Prepare your source and target CSV files containing the data you want to reconcile, i have that in my repository.

   - And Ensure that the column names in the CSV files match the expected column names used in the reconciliation script.

3. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the reconciliation script (`reconciliation_script.py`).
   - Run the script with the following command to compare all column:
     ```
     python reconciliation_script.py -s source.csv -t target.csv -o output.csv -c 
     ```
     - Replace `source.csv` and `target.csv` with the paths to your source and target CSV files.
     - Replace `output.csv` with the desired filename/path for the reconciliation report.
     - Optionally, specify the columns you want to compare using the `-c` or `--columns` argument.
     ```
     python reconciliation_script.py -s source.csv -t target.csv -o output.csv -c Column1 Column2 Column3
     ```

4. **Viewing the Reconciliation Report:**
   - After running the script, the reconciliation report will be generated and saved to the specified output CSV file.
    ![Reconciliation Process](https://res.cloudinary.com/tracysoft/image/upload/v1712309678/Screenshot_2024-04-05_at_10.31.40_AM.png)
   
### Running Unit Tests:

1. **Prepare Test Data:**
   - Ensure that you have sample CSV files (`sample_source.csv` and `sample_target.csv`) containing test data, i have added that to my repo.

2. **Run Unit Tests:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the reconciliation script and the test file (`test_reconciliation_script.py`).
   - Run the unit tests with the following command:
     ```
     python -m unittest test_reconciliation_script
     ```
     - This command will discover and execute the test cases defined in the test file.
     - You would see the test results indicating whether the tests passed or failed.
    ![Reconciliation Process](https://res.cloudinary.com/tracysoft/image/upload/v1712309678/Screenshot_2024-04-05_at_10.12.22_AM.png)


