import pandas as pd
import glob
import os

RAW_FOLDER = "data_raw"
CLEANED_FOLDER = "data_cleaned"

def load_and_combine():
    files = glob.glob(os.path.join(RAW_FOLDER, "*.xlsx"))
    df_list = []

    for file in files:
        print(f"Loading: {os.path.basename(file)}")
        df = pd.read_excel(file)
        df_list.append(df)

    combined = pd.concat(df_list, ignore_index=True)
    return combined

def clean_data(df):
    # Trim spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Remove duplicates
    df = df.drop_duplicates()

    # Example: Convert date columns (if exist)
    date_cols = [c for c in df.columns if "date" in c]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def save_output(df):
    os.makedirs(CLEANED_FOLDER, exist_ok=True)
    output_path = os.path.join(CLEANED_FOLDER, "cleaned_master.xlsx")
    df.to_excel(output_path, index=False)
    print(f"\n✅ Cleaned file saved → {output_path}")

if __name__ == "__main__":
    combined_df = load_and_combine()
    cleaned_df = clean_data(combined_df)
    save_output(cleaned_df)
