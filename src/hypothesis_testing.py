from scipy import stats
import pingouin as pg

def test_province_risk_difference(df):
    provinces = df['Province'].value_counts().head(6).index
    groups = [df[df['Province'] == p]['TotalClaims'] / df[df['Province'] == p]['TotalPremium'] for p in provinces]
    f_stat, p_val = stats.f_oneway(*groups)
    print(f"Province Risk Difference Test: F={f_stat:.2f}, p={p_val:.2e}")
    return p_val < 0.05

def test_gender_risk_difference(df):
    male = df[df['Gender'] == 'Male']['TotalClaims'] / df[df['Gender'] == 'Male']['TotalPremium']
    female = df[df['Gender'] == 'Female']['TotalClaims'] / df[df['Gender'] == 'Female']['TotalPremium']
    t_stat, p_val = stats.ttest_ind(male.dropna(), female.dropna(), equal_var=False)
    print(f"Gender Risk Difference: t={t_stat:.2f}, p={p_val:.2e}")
    return p_val < 0.05

# Run tests
print("Hypothesis Testing Results:")
print("H0: No risk differences across provinces →", "REJECTED" if test_province_risk_difference(df) else "Failed to reject")
print("H0: No risk difference between men and women →", "REJECTED" if test_gender_risk_difference(df) else "Failed to reject")