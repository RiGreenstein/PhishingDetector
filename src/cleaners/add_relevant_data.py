import pandas as pd

df_old = pd.read_csv("data/processed/2014_data_cleaned.csv", encoding="utf-8", encoding_errors="replace", engine="python")
df_new = pd.read_csv("data/processed/2026_data_cleaned.csv", encoding="utf-8", encoding_errors="replace", engine="python")

# Helper functions
def getCharacterFrequency(char, column, df):
    for i, row in df.iterrows():
        df.iloc[i-1, column] = row["url"].count(char)

    return df

# 2014 Data

# Url length
df_old["url_len"] = df_old["url"].str.len()

# Character counts
df_old["periods"] = getCharacterFrequency(".", 4, df_old)
#getCharacterFrequency("-", "hyphens", df_old)
#getCharacterFrequency("/", "slashes", df_old)
#getCharacterFrequency("?", "questions", df_old)
#getCharacterFrequency("&", "ampersand", df_old)

df_old.to_csv("data/processed/2014_data_cleaned.csv", index=False)
# When I come back turn get character frequency into returning a series
