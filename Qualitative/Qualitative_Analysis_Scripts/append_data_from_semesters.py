import pandas as pd

if __name__ == '__main__':
    files = [
        "SP22_Cleaned_Categorized_v2.csv",
        "FA22_Cleaned_Categorized_v2.csv",
        "SP23_Cleaned_Categorized_v2.csv",
        "FA23_Cleaned_Categorized_v2_v2.csv",
        "SP24_Cleaned_Categorized_v2.csv",
        "FA24_Cleaned_Categorized_v2.csv",
        "SP25_Cleaned_Categorized_v2.csv",
        "FA25_Cleaned_Categorized_v2.csv",
    ]

    # Read and append all CSV files in the specified order
    dfs = [pd.read_csv(file) for file in files]
    combined_df = pd.concat(dfs, ignore_index=True)

    # Add IDs starting from 1
    combined_df.insert(0, "ID", range(1, len(combined_df) + 1))

    # Save the final CSV
    combined_df.to_csv("SP22_FA25_Cleaned_Combined.csv", index=False)

    print(f"Saved {len(combined_df)} rows to SP22_FA25_Cleaned_Combined.csv")