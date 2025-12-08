import pandas as pd

def process_data(input_path, output_path):
    try:
        # Specify the correct delimiter as '|'
        df = pd.read_csv(input_path, sep='|', on_bad_lines='skip')
        print(df.columns.tolist())  # Print column names for debugging
        
        # Strip whitespace from column names if necessary
        df.columns = df.columns.str.strip()
        
        # Check if the 'TransactionMonth' column exists before processing
        if 'TransactionMonth' in df.columns:
            df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
        else:
            print("Column 'TransactionMonth' not found in DataFrame")
            return

        # Ensure 'PostalCode' is treated as a string
        if 'PostalCode' in df.columns:
            df['PostalCode'] = df['PostalCode'].astype(str)
        
        # Adding a new feature 'NewFeature', simulating an update based on 'TotalPremium'
        if 'TotalPremium' in df.columns:
            df['NewFeature'] = df['TotalPremium'] * 1.1  # Example modification
        else:
            print("Column 'TotalPremium' not found in DataFrame")
        
        # Save the processed DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_data(
        r"C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\raw\insurance_data_feb2014_aug2015.txt", 
        r"C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\processed\insurance_cleaned_dataset.csv"
    )