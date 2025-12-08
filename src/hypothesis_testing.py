import pandas as pd
import numpy as np
from scipy import stats
import pingouin as pg  # For Welch's t-test if variances unequal

def load_aggregated_data(path='data/processed/policy_aggregated.csv'):
    return pd.read_csv(path)

def check_group_balance(df, group_col, balance_cols=['VehicleType', 'Make']):
    for col in balance_cols:
        contingency = pd.crosstab(df[group_col], df[col])
        chi2, p, _, _ = stats.chi2_contingency(contingency)
        print(f"Balance check for {col} across {group_col}: chi2={chi2:.2f}, p={p:.4f}")
    # Add mean comparisons if numerical balance cols

def test_frequency_difference(df, group_col):
    contingency = pd.crosstab(df[group_col], df['HasClaim'])
    if contingency.shape[0] < 2 or contingency.sum().min() < 5:
        return np.nan, np.nan
    chi2, p, _, _ = stats.chi2_contingency(contingency)
    return chi2, p

def test_severity_difference(df, group_col):
    claimants = df[df['HasClaim'] == 1]
    groups = [claimants[claimants[group_col] == g]['ClaimAmount'].dropna() for g in claimants[group_col].unique()]
    groups = [g for g in groups if len(g) > 1 and g.var() > 0]  # Skip invalid groups
    if len(groups) < 2:
        return np.nan, np.nan
    f, p = stats.f_oneway(*groups)
    return f, p

def test_margin_difference(df, group_col):
    groups = [df[df[group_col] == g]['Margin'].dropna() for g in df[group_col].unique()]
    groups = [g for g in groups if len(g) > 1 and g.var() > 0]
    if len(groups) < 2:
        return np.nan, np.nan
    f, p = stats.f_oneway(*groups)
    return f, p

def test_gender_risk(df):
    df_gender = df[df['Gender'].isin(['Male', 'Female'])]
    # Frequency
    chi2_freq, p_freq = test_frequency_difference(df_gender, 'Gender')
    # Severity (Welch's t-test for unequal var)
    claimants = df_gender[df_gender['HasClaim'] == 1]
    male_sev = claimants[claimants['Gender'] == 'Male']['ClaimAmount'].dropna()
    female_sev = claimants[claimants['Gender'] == 'Female']['ClaimAmount'].dropna()
    t_sev, p_sev = stats.ttest_ind(male_sev, female_sev, equal_var=False)
    return (chi2_freq, p_freq), (t_sev, p_sev)

def run_all_tests():
    df = load_aggregated_data()
    
    # Limit zipcodes to top 10 for feasibility
    top_zips = df['PostalCode'].value_counts().head(10).index
    df_zip = df[df['PostalCode'].isin(top_zips)]
    
    # Check balance (example for provinces)
    check_group_balance(df, 'Province')
    
    results = {}
    
    # H1: Provinces risk
    chi2_freq, p_freq = test_frequency_difference(df, 'Province')
    f_sev, p_sev = test_severity_difference(df, 'Province')
    results['H1'] = {'freq_p': p_freq, 'sev_p': p_sev}
    
    # H2: Zipcodes risk (top 10)
    chi2_freq, p_freq = test_frequency_difference(df_zip, 'PostalCode')
    f_sev, p_sev = test_severity_difference(df_zip, 'PostalCode')
    results['H2'] = {'freq_p': p_freq, 'sev_p': p_sev}
    
    # H3: Zipcodes margin (top 10)
    f_margin, p_margin = test_margin_difference(df_zip, 'PostalCode')
    results['H3'] = {'margin_p': p_margin}
    
    # H4: Gender risk
    (chi2_freq, p_freq), (t_sev, p_sev) = test_gender_risk(df)
    results['H4'] = {'freq_p': p_freq, 'sev_p': p_sev}
    
    # Print results
    for h, res in results.items():
        print(f"{h}: {res}")
    
    return results

if __name__ == "__main__":
    run_all_tests()