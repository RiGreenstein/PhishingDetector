import pandas as pd
df = pd.read_csv("data/2014_data.csv", encoding="latin1", low_memory=False, on_bad_lines='skip')

print(df.shape)
print(df.columns.to_list())
print(df["label"].value_counts()) 