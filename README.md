# AlphaCare Insurance Solutions - Risk Analytics & Predictive Modeling

## Objective
his repository contains the code, analysis, and reports for the AlphaCare Insurance Risk Analytics & Predictive Modeling project. The goal is to analyze historical car insurance claim data from South Africa (February 2014 to August 2015) to identify low-risk customer segments, optimize premiums, and support marketing strategies. This helps AlphaCare Insurance Solutions (ACIS) attract new clients by reducing premiums for low-risk targets.



## Project Structure
      alphacare-insurance-analytics/
      ├── data/
      │   ├── raw/                  # Raw dataset (insurance_data_feb2014_aug2015.xlsx)
      │   └── processed/            # Cleaned/processed data files
      ├── notebooks/
      │     └── 01_eda_exploration.ipynb  # Jupyter notebook for EDA and initial stats
      ├── src/
      │   ├── data_loader.py        # Data loading utilities
      │   ├── eda.py                # EDA functions
      │   ├── hypothesis_testing.py # Hypothesis testing scripts
      │   ├── modeling.py           # Predictive modeling code
      │   └── utils.py              # Helper utilities
      ├── reports/
      │   └── eda_report.pdf        # Summary report of EDA and statistical findings
      ├── output/
      │   ├── loss_ratio_by_province.png
      │   ├── claims_vs_premium_gender.png
      │   ├── top_risky_makes.png
      │   └── feature_importance.png
      ├── tests/                    # Unit tests (e.g., for data loading and models)
      ├── requirements.txt          # Python dependencies
      ├── README.md                 # This file
      └── .github/workflows/ci.yml  # CI/CD pipeline for GitHub Actions

### 🚀 Setup and Installation
  1. Clone the Repository
       git clone https://github.com/yourusername/alphacare-insurance-analytics.git
       cd alphacare-insurance-analytics

  2. Create and Activate a Virtual Environment
     
      Windows
      python -m venv venv
      venv\Scripts\activate

 3. Install Dependencies
      pip install -r requirements.txt

 4. Add the Raw Data

      Download the raw dataset and place it in:
      data/raw/

 5. Run the EDA Notebook
       jupyter notebook notebooks/01_eda_exploration.ipynb

### 📘 Task 1 — Git, GitHub, EDA & Statistical Analysis

 Task 1 establishes the foundation of the project, including environment setup, version control practices, exploratory analysis, and statistical testing.
 A dedicated branch was used:

       task-1-eda-stats


#### 🔍 Key Activities
 1. Data Understanding & EDA

 - Loaded and explored the dataset.
 - Performed descriptive statistics, missing-value checks, and outlier detection.
 - Conducted univariate and bivariate analysis.
 - Explored relationships across regions, vehicle classes, and demographics.
 - Created visual insights saved in output/.

 2. Statistical Analysis
 - Computed loss ratios.
 - Used boxplots and histograms for risk distribution analysis.
 - Performed hypothesis tests on risk differences.

 3. Visualizations (3 Highlighted Plots)
 - Loss Ratio by Province
 - Claims vs Premium by Gender (log scale)
 - Top 10 Riskiest Vehicle Makes

 4. Initial Modeling

 - Built a simple Random Forest model.
 - Extracted feature importances to understand premium drivers.

----
```markdown
# 🧩 Task 2 — Reproducible Data Pipeline with DVC

In regulated industries—such as insurance, banking, lending, and healthcare—every dataset used to produce a model or analysis must be traceable and reproducible. DVC (Data Version Control) ensures datasets are version-controlled with the same rigor as code.

## ✅ 1. Install DVC
```bash
pip install dvc
```

### Initialize DVC in the project root:
```bash
dvc init
```

## ✅ 2. Configure Local Remote Storage

Create a directory for DVC-managed storage:
```bash
mkdir /path/to/local/storage
```

Add it as your default remote:
```bash
dvc remote add -d localstorage /path/to/local/storage
```

## ✅ 3. Add Data Files to DVC

Place raw datasets into the `data/raw/` directory and track them:
```bash
dvc add data/raw/portfolio.csv
dvc add data/raw/claims.csv
```

This generates `.dvc` pointer files. Commit them:
```bash
git add data/raw/*.dvc .gitignore
git commit -m "Tracked datasets with DVC"
```

## ✅ 4. Push Data to Remote
```bash
dvc push
```

Your dataset is now fully versioned and reproducible.


---

# 🧪 Task 3 — Statistical Hypothesis Testing & Risk Segmentation

This task evaluates whether features such as province, postal code, gender, and vehicle make drive meaningful risk differences.

## 🎯 Risk Metrics Used
- **Claim Frequency**: Fraction of policies with ≥ 1 claim.
- **Claim Severity**: Average cost of a claim (conditional on claiming).
- **Margin**: TotalPremium − TotalClaims.

## 🎯 Null Hypotheses Evaluated
| Hypothesis | Feature         | Objective                                        |
|------------|-----------------|--------------------------------------------------|
| H₀₁       | Province        | No risk differences across provinces               |
| H₀₂       | Postal Code     | No risk differences between zip codes             |
| H₀₃       | Margin          | No profit difference across zip codes             |
| H₀₄       | Gender          | No risk difference between genders                |

## 🧭 Steps Followed
1️⃣ **Select KPIs**
   - Claim Frequency
   - Claim Severity
   - Margin (profitability)

2️⃣ **Build A/B Groups**
   - Group A = Control
   - Group B = Test
   - Validated group equivalence using Standardized Mean Difference (SMD < 0.1)

3️⃣ **Statistical Tests**
   - Chi-square → Frequency differences
   - Mann–Whitney / Kruskal–Wallis → Severity
   - Z-test for Proportions
   - Bootstrap Confidence Intervals
   - Bonferroni-corrected pairwise comparisons

4️⃣ **Report & Interpret**
   Results fully documented below.

## 📊 Full Risk & Profitability Analysis Report (Task 3)

### 1. Overview
This analysis evaluates claim frequency, severity, and overall profitability across multiple customer segments.

**Portfolio-level Metrics**
- Overall Claim Frequency: 0.00279
- Average Severity: 23,273.39
- Total Margin: –2,955,983 (negative → portfolio underpriced)

### 2. Provincial Differences (H₀₁)
**Result**: Null rejected for both frequency and severity.
- **Claim Frequency (High → Low)**: Gauteng, KwaZulu-Natal, ... Northern Cape, Free State
- **Claim Severity (High → Low)**: Free State, KwaZulu-Natal, ... Northern Cape, Limpopo

**Conclusion**: Provinces must be included in the pricing model.

### 3. Zip Code Differences (H₀₂ & H₀₃)
**Result**: Strong rejection for both frequency and margin.
- Frequency Chi-square: p < 0.000001
- Margin Kruskal–Wallis: p < 0.000001

**Conclusion**: Postal code = strongest geographical predictor of insurance risk.

### 4. Gender Differences (H₀₄)
**Result**: Fail to reject.
- Frequency: p = 0.951
- Severity: p = 0.223

**Conclusion**: Gender does not influence risk → remove from pricing.

### 5. Vehicle Make & Severity
- Large variation observed across makes.
- Gender effect negligible.
- Some makes show extreme severity (small N).

**Conclusion**: Vehicle make is a valid pricing factor.

### 6. A/B Segmentation Summary
- Groups well balanced (SMD < 0.1).
- Frequency differs: p = 0.013.
- Severity: borderline, but bootstrap confirms real difference.

### 7. Portfolio Recommendations
**Pricing**:
- Add province + postal code relativity factors.
- Adjust vehicle make loadings.

**Underwriting**:
- Investigate high-loss zip codes.
- Analyze severity-heavy regions.

---

# 🤖 Task 4 — Predictive Modeling for Risk-Based Pricing

Build claim severity and premium optimization models that form the basis of a pricing engine.

## 🧭 1. Data Preparation
**Handling Missing Data**:
- Imputed numeric fields.
- Filled categorical NAs with "Unknown".

**Feature Engineering**:
- Vehicle age.
- Claim indicator.
- Log-severity.
- Geography × Vehicle interactions.

**Encoding**:
```python
pd.get_dummies(df, drop_first=True)
```

**Train-Test Split**:
```python
train, test = train_test_split(df, test_size=0.2, random_state=42)
```

## 🧠 2. Models Built
🔹 **Severity Model (Regression)**:
- Linear Regression.
- Random Forest Regressor.
- XGBoost Regressor.
- Metrics: RMSE, R².

🔹 **Claim Probability Model (Classification)**:
- Logistic Regression.
- Random Forest Classifier.
- XGBoost Classifier.
- Metrics: AUC, Recall, Precision, F1.

🔹 **Combined Premium Model (Conceptual)**:
- Premium = P(Claim) × Predicted Severity + Expense Loading + Profit Margin.

## 📊 3. Model Evaluation
| Model                 | RMSE  | R²   | Notes                        |
|-----------------------|-------|------|------------------------------|
| Linear Regression      | High  | Low  | Baseline only                |
| Random Forest          | Lower | Better | Handles non-linearity      |
| XGBoost                | Best  | Highest | Recommended                |

## 🔍 4. Model Interpretability (SHAP)
**Key insights**:
- Older vehicles → significantly higher severity.
- Certain makes → higher predicted cost.
- Province contributes strongly to both severity & claim probability.

**Business Interpretation Example**:
“Each additional year of vehicle age increases expected severity by ~X Rand, validating the need for stronger age-based rating factors.”

## 🟩 Minimum Requirements Completed
- Task 3 merged into main via PR.
- New branch `task-4` created.
- Clean, descriptive commits.
- Full data preparation pipeline.
- Multiple predictive models implemented.
- Evaluation using RMSE, R², AUC.
- SHAP interpretability delivered.

## ✅ Final Summary
This project now includes:
- A fully reproducible dataset pipeline using DVC.
- A statistically validated segmentation of geographical & vehicle risk.
- Predictive models for both claim probability and severity.
- A business-ready premium framework grounded in statistical and actuarial rigor.


```

