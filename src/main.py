import pandas as pd
df = pd.read_csv("data/raw/2026_data.csv", encoding="latin1", low_memory=False, on_bad_lines="skip")

print(df.shape)
print(df.columns.to_list())
#print(df["url"].value_counts())