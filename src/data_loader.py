import pandas as pd

def load_data(path=r'C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\raw\insurance_data_feb2014_aug2015.csv'):
    print(f"Attempting to load data from: {path}")
    try:
        # Read the text file; adjust the delimiter if necessary
        df = pd.read_csv(path, delimiter='\t')  # Use appropriate delimiter based on the file structure
        print(f"Data loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print("The specified file was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")

def basic_info(df):
    print("\nData Types & Missing Values:")
    print(df.info())
    print("\nMissing Values (%):")
    print(df.isnull().mean() * 100)

if __name__ == "__main__":
    data = load_data()
    if data is not None:
        basic_info(data)

    