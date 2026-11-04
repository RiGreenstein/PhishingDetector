import pandas as pd
df = pd.read_csv("processed_data/2014_data_cleaned.csv", encoding="latin1", low_memory=False)

print(df.shape)
print(df.columns.to_list())
print(df["label"].value_counts())