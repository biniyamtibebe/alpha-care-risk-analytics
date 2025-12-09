import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm

# Example of defining dtypes, adjust these according to your actual data
dtype_dict = {
    'PostalCode': 'category',  # Use category for less frequent values
    'TotalPremium': 'float32',
    'TotalClaims': 'float32',
    # Add other columns as needed
}

chunk_size = 100000  # Adjust based on your memory capacity
data_iterator = pd.read_csv(r"C:\Users\hp\Pictures\AlphaCare Insurance Solutions (ACIS)\alpha-care-risk-analytics\data\processed\insurance_cleaned_dataset.csv", 
                             parse_dates=['TransactionMonth'], 
                             chunksize=chunk_size, 
                             low_memory=False,
                             dtype=dtype_dict)

# Process each chunk
df_list = []
for chunk in data_iterator:
    df_list.append(chunk)

# Combine all chunks into a single DataFrame
df = pd.concat(df_list)
# Quick sanity
print("Rows:", len(df))
print(df.columns)

#2. Define KPIs ----------
# Binary: did policy have at least one claim
df['has_claim'] = (df['totalclaims'] > 0).astype(int)

# Claim severity: average claim amount conditional on a claim
# We'll compute groupwise statistics later using df_claims
df_claims = df[df['has_claim'] == 1].copy()

# Margin
df['margin'] = df['totalpremium'] - df['totalclaims']

# Basic check
print("Overall claim frequency:", df['has_claim'].mean())
print("Overall avg severity (given claim):", df_claims['totalclaims'].mean())
print("Overall margin (sum):", df['margin'].sum())

# ---------- 3. Helper functions ----------
def print_header(msg):
    print("\n" + "="*6 + " " + msg + " " + "="*6)

def summarize_group_kpis(data, group_col):
    # Returns summary table with counts, freq, severity (conditional), margin mean/median
    groups = data.groupby(group_col).agg(
        policies=('has_claim', 'count'),
        claims_count=('has_claim', 'sum'),
        total_claims_amount=('totalclaims', 'sum'),
        total_premium=('totalpremium', 'sum'),
        avg_margin=('margin', 'mean')
    ).reset_index()
    groups['claim_freq'] = groups['claims_count'] / groups['policies']
    # severity: total_claims_amount / claims_count (avoid div by 0)
    groups['claim_severity'] = groups.apply(
        lambda r: (r['total_claims_amount'] / r['claims_count']) if r['claims_count']>0 else np.nan, axis=1)
    groups['loss_ratio'] = groups['total_claims_amount'] / groups['total_premium']
    return groups

def smd_continuous(a, b):
    # standardized mean difference for continuous variables
    return (a.mean() - b.mean()) / np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2)

def smd_binary(a, b):
    # smd for binary proportion
    pa = a.mean()
    pb = b.mean()
    pooled = np.sqrt((pa*(1-pa) + pb*(1-pb)) / 2)
    return (pa - pb) / pooled