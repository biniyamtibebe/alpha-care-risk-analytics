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

