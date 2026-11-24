
import pandas as pd


def clean_agent_data(txns, agents):
    """
    Clean agent transaction data and return a cleaned DataFrame
    together with a log of cleaning actions.
    """

    clean_df = txns.copy()
    log = []

    # 1. Remove duplicate transaction IDs
    duplicates = clean_df.duplicated(subset="txn_id").sum()
    clean_df = clean_df.drop_duplicates(
        subset="txn_id", keep="first"
    ).copy()

    log.append({
        "action": "Removed duplicate transaction IDs",
        "rows_affected": int(duplicates)
    })

    # 2. Standardise transaction types
    clean_df["txn_type"] = (
        clean_df["txn_type"]
        .astype("string")
        .str.strip()
        .str.lower()
        .map({
            "deposit": "Deposit",
            "withdrawal": "Withdrawal"
        })
    )

    log.append({
        "action": "Standardised transaction types",
        "rows_affected": int(clean_df["txn_type"].notna().sum())
    })

    # 3. Convert amounts to numeric
    clean_df["amount"] = pd.to_numeric(
        clean_df["amount"], errors="coerce"
    )

    # Track missing amounts before imputation
    clean_df["amount_imputed"] = clean_df["amount"].isna()
    missing_amounts = int(clean_df["amount_imputed"].sum())

    # Impute using median for each transaction type
    medians = clean_df.groupby("txn_type")["amount"].transform("median")
    clean_df["amount"] = clean_df["amount"].fillna(medians)

    log.append({
        "action": "Imputed missing transaction amounts",
        "rows_affected": missing_amounts
    })

    # 4. Convert transaction dates
    clean_df["txn_date"] = pd.to_datetime(
        clean_df["txn_date"],
        format="mixed",
        errors="coerce"
    )

    log.append({
        "action": "Converted transaction dates",
        "rows_affected": int(clean_df["txn_date"].notna().sum())
    })

    # 5. Detect outliers using IQR
    q1 = clean_df["amount"].quantile(0.25)
    q3 = clean_df["amount"].quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    clean_df["is_outlier"] = (
        (clean_df["amount"] < lower_limit) |
        (clean_df["amount"] > upper_limit)
    )

    log.append({
        "action": "Flagged potential amount outliers",
        "rows_affected": int(clean_df["is_outlier"].sum())
    })

    # 6. Merge county information
    clean_df = clean_df.merge(
        agents[["agent_id", "county"]],
        on="agent_id",
        how="left"
    )

    unknown_agents = int(clean_df["county"].isna().sum())

    log.append({
        "action": "Merged agent county information",
        "rows_affected": unknown_agents
    })

    # Return cleaned data and cleaning log
    log_df = pd.DataFrame(log)

    return clean_df, log_df
