# Duka Sales and Agent Network Data Analysis

## Project Overview

This project contains two data analytics engagements:

1. Duka Electronics sales exploration and business reporting.
2. Agent network transaction data cleaning, validation and analysis.

The project uses Python, pandas, NumPy and Excel to demonstrate data generation, data quality assessment, data cleaning, analysis and reporting.

## 1. Duka Electronics Sales Analysis

### Executive Summary

The analysis covered 1,000 sales transactions across five branches from January to June 2026.

Nairobi recorded the highest branch revenue of KES 26,106,100, while Eldoret recorded the lowest at KES 8,844,200.

Laptops generated the highest product revenue of KES 41,535,000.

April was the strongest month, generating KES 13,518,300, while June recorded the lowest monthly revenue of KES 10,903,400.

The Premium Online segment across Nairobi and Mombasa contained 83 transactions worth KES 10,218,000.

### Files

- `duka_sales_exploration.ipynb`: Sales exploration and analysis.
- `excel/duka_branch_summary.xlsx`: Branch revenue analysis and PivotTable.
- `outputs/premium_online_coast_capital.csv`: Filtered Premium Online transactions for Nairobi and Mombasa.

### Regenerating and Running

1. Install dependencies using `pip install -r requirements.txt`.
2. Run `python generate_data.py` to generate the datasets.
3. Open `duka_sales_exploration.ipynb` in Google Colab or Jupyter.
4. Upload the generated `duka_sales.csv` and run the notebook from top to bottom.

## 2. Agent Network Data Cleaning

### Data Overview

The original agent register contains 20 agents.

The original transaction dataset contains 612 rows. After removing 12 duplicate transaction IDs, 600 unique transactions remain.

### Cleaning and Analysis

The cleaning process includes:

- Duplicate transaction identification and removal.
- Standardisation of transaction types.
- Numeric conversion of transaction amounts.
- Transaction date standardisation.
- Median imputation of missing amounts.
- IQR-based outlier detection.
- Merging transactions with agent county information.
- Identification of unknown agent references.
- County and weekly transaction summaries.

The pipeline identifies 20 imputed amounts, 53 potential outliers and 7 transactions associated with the unknown agent AG099.

### Files

- `agent_cleanup.ipynb`: Data audit, cleaning and analysis.
- `cleaning_pipeline.py`: Reusable transaction cleaning function.
- `outputs/agent_transactions_clean.csv`: Cleaned transaction dataset.

### Regenerating and Running

1. Run `python generate_data.py` to regenerate the agent datasets.
2. Open `agent_cleanup.ipynb` in Google Colab or Jupyter.
3. Make sure `agents.csv`, `agent_transactions.csv` and `cleaning_pipeline.py` are available in the notebook environment.
4. Run the notebook from top to bottom.

## 3. Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 4. Repository Structure

```text
plp-da-a3-duka-sales-and-agent-cleanup/
│
├── README.md
├── requirements.txt
├── generate_data.py
├── cleaning_pipeline.py
├── duka_sales_exploration.ipynb
├── agent_cleanup.ipynb
│
├── excel/
│   └── duka_branch_summary.xlsx
│
└── outputs/
    ├── premium_online_coast_capital.csv
    └── agent_transactions_clean.csv
```

## 5. Data Privacy

The project avoids publishing the original raw datasets. If customer phone numbers or other personal information were present, they would require appropriate protection under Kenya's Data Protection Act, 2019. Public reporting should use aggregated or anonymised information where possible.

## Disclaimer

This is an educational data analytics project. The datasets are generated for learning and analysis purposes.