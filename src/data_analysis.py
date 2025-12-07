import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Load data
file_path = r"C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\raw\insurance_data_feb2014_aug2015.csv"

try:
    df = pd.read_excel(file_path, engine='openpyxl')
    print("File loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Proceed if the DataFrame was successfully created
if 'df' in locals():
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    df['PostalCode'] = df['PostalCode'].astype(str)
    df['TotalPremium'] = df['TotalPremium'].abs()
    df['TotalClaims'] = df['TotalClaims'].abs()

    # Overall Loss Ratio Calculation
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, np.nan)

    # Calculating overall loss ratio
    overall_loss_ratio = df['TotalClaims'].sum() / df['TotalPremium'].sum() if df['TotalPremium'].sum() != 0 else np.nan
    print(f"Overall Portfolio Loss Ratio: {overall_loss_ratio:.3f}")
else:
    print("DataFrame 'df' is not defined. Check the file loading step.")