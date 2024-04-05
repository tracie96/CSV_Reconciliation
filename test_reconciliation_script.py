import os
import unittest

import pandas as pd

from reconciliation_script import parse_csv, identify_missing_records, compare_fields, generate_report

class TestReconciliationScript(unittest.TestCase):
    def setUp(self):
        # I have created a sample dataframes for testing
        self.source_df = parse_csv('sample_source.csv')
        self.target_df = parse_csv('sample_target.csv')

    def test_parse_csv(self):
        # Test if parse_csv function returns a DataFrame
        self.assertIsInstance(self.source_df, pd.DataFrame)
        self.assertIsInstance(self.target_df, pd.DataFrame)

    def test_identify_missing_records(self):
        # Test if identify_missing_records function returns the expected results
        missing_in_target, missing_in_source = identify_missing_records(self.source_df, self.target_df)

        self.assertEqual(len(missing_in_target), 1)  # Assuming one record is missing in the target

    def test_compare_fields(self):
        # Test if compare_fields function returns the expected results
        columns_to_compare = ['Date']  # Assuming these are the columns to compare

        discrepancies = compare_fields(self.source_df, self.target_df, columns_to_compare)

        self.assertEqual(len(discrepancies), 1)  # Assuming one discrepancy is found

    def test_generate_report(self):
        # Test if generate_report function generates the output CSV file
        output_file = 'test_output.csv'

        # Assuming there are some missing records and discrepancies
        missing_in_target = pd.DataFrame({'ID': [1], 'Column1': ['Value1'], 'Column2': ['Value2']})
        missing_in_source = pd.DataFrame()
        discrepancies = pd.DataFrame({'ID': [2], 'Field': ['Column1'], 'Source Value': ['Value1'], 'Target Value': ['Value2']})

        generate_report(missing_in_target, missing_in_source, discrepancies, output_file)

        # Check if the output CSV file is created
        self.assertTrue(os.path.exists(output_file))

    def tearDown(self):
        # Clean up by removing the output file created during testing
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')

if __name__ == '__main__':
    unittest.main()
