import pandas as pd

def process_data(input_path, output_path):
    try:
        # Specify the correct delimiter as '|'
        df = pd.read_csv(input_path, sep='|', on_bad_lines='skip')
        print(df.columns.tolist())  # Print column names for debugging
        
        # Strip whitespace from column names if necessary
        df.columns = df.columns.str.strip()
        
        # Check if the column exists before processing
        if 'TransactionMonth' in df.columns:
            df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
        else:
            print("Column 'TransactionMonth' not found in DataFrame")
            return
        
        df['PostalCode'] = df['PostalCode'].astype(str)
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_data(
        r"C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\raw\insurance_data_feb2014_aug2015.txt", 
        r"C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\processed\insurance_cleaned_dataset.csv"
    )