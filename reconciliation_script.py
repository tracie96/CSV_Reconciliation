import argparse
import csv
import pandas as pd
from tabulate import tabulate #to display table on terminal

def parse_csv(file_path):
    #Parse CSV file to return a DataFrame.
    return pd.read_csv(file_path)


def identify_missing_records(source_df, target_df):
    #Here i am trying to identify missing gecords and target.
    missing_in_target = source_df[~source_df['ID'].isin(target_df['ID'])]
    missing_in_source = target_df[~target_df['ID'].isin(source_df['ID'])]
    return missing_in_target, missing_in_source


def compare_fields(source_df, target_df, columns_to_compare):
    common_ids = set(source_df['ID']).intersection(target_df['ID'])
    discrepancies = pd.DataFrame(columns=['ID', 'Field', 'Source Value', 'Target Value'])
    for id in common_ids:
        source_row = source_df.loc[source_df['ID'] == id]
        target_row = target_df.loc[target_df['ID'] == id]

        for col in columns_to_compare:
            if source_row[col].values[0] != target_row[col].values[0]:
                discrepancies = pd.concat([discrepancies, pd.DataFrame({
                    'ID': [id],
                    'Field': [col],
                    'Source Value': [source_row[col].values[0]],
                    'Target Value': [target_row[col].values[0]]
                })], ignore_index=True)

    return discrepancies


def generate_report(missing_in_target, missing_in_source, discrepancies, output_file):
    #Generating a report
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Type', 'Record Identifier', 'Field', 'Source Value', 'Target Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for idx, row in missing_in_target.iterrows():
            writer.writerow({'Type': 'Missing in Target', 'Record Identifier': row['ID'], 'Field': '', 'Source Value': '', 'Target Value': ''})

        for idx, row in missing_in_source.iterrows():
            writer.writerow({'Type': 'Missing in Source', 'Record Identifier': '', 'Field': row['ID'], 'Source Value': '', 'Target Value': ''})

        for idx, row in discrepancies.iterrows():
            writer.writerow({'Type': 'Field Discrepancy', 'Record Identifier': row['ID'], 'Field': row['Field'],
                             'Source Value': row['Source Value'], 'Target Value': row['Target Value']})

    print("Reconciliation completed:")
    print(f"- Records missing in target: {len(missing_in_target)}")
    print(f"- Records missing in source: {len(missing_in_source)}")
    print(f"- Records with field discrepancies: {len(discrepancies)}")
    print(f"Report saved to: {output_file}")

    # Display output CSV contents in tabular form in terminal
    output_df = pd.read_csv(output_file)
    print(tabulate(output_df, headers='keys', tablefmt='psql'))


def main(source_file, target_file, output_file, columns_to_compare=None):
    source_df = parse_csv(source_file)
    target_df = parse_csv(target_file)

    missing_in_target, missing_in_source = identify_missing_records(source_df, target_df)

    if columns_to_compare is None:
        columns_to_compare = source_df.columns[1:]  # Excluding the 'ID' column

    discrepancies = compare_fields(source_df, target_df, columns_to_compare)

    generate_report(missing_in_target, missing_in_source, discrepancies, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV Reconciliation Tool")
    parser.add_argument("-s", "--source", help="Path to source CSV file")
    parser.add_argument("-t", "--target", help="Path to target CSV file")
    parser.add_argument("-o", "--output", help="Path to save the output reconciliation report")
    parser.add_argument("-c", "--columns", nargs='+', help="Columns to compare during reconciliation", default=None)
    args = parser.parse_args()

    main(args.source, args.target, args.output, args.columns)
