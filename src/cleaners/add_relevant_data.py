import pandas as pd

df_old = pd.read_csv("data/processed/2014_data_cleaned.csv", encoding="utf-8", encoding_errors="replace", engine="python")
df_new = pd.read_csv("data/processed/2026_data_cleaned.csv", encoding="utf-8", encoding_errors="replace", engine="python")

# Helper functions
def getCharacterFrequency(char, df):
    total_count = pd.Series(0, index=df.index)

    for i in char:
        total_count += df["url"].str.count(i)

    return total_count

# 2014 Data

# Url length
df_old["url_len"] = df_old["url"].str.len()

# Hostname length
df_old["hostname_len"] = df_old["url"].apply(
    lambda x: len(x[x.find(".") + 1 : x.find("/")])
)

# Path length
df_old["path_len"] = df_old["url"].apply(
    lambda x: len(x[x.find("/"):]) if "/" in x else 0
)

# Character counts
df_old["periods"] = getCharacterFrequency([r"\."], df_old)
df_old["hyphens"] = getCharacterFrequency(["-"], df_old)
df_old["slashes"] = getCharacterFrequency(["/"], df_old)
df_old["questions"] = getCharacterFrequency([r"\?"], df_old)
df_old["ampersands"] = getCharacterFrequency(["&"], df_old)
df_old["ats"] = getCharacterFrequency(["@"], df_old)
df_old["underscores"] = getCharacterFrequency(["_"], df_old)
df_old["percentages"] = getCharacterFrequency(["%"], df_old)

# Digit count
df_old["digits"] = getCharacterFrequency(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], df_old)

df_old.to_csv("data/processed/2014_data_cleaned.csv", index=False)