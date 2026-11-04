import pandas as pd
df = pd.read_csv("data/processed/2026_data_cleaned.csv", encoding="latin1", low_memory=False, on_bad_lines="skip")
old_lengths_phishing = []
old_lengths_legit = []

#print(df["url"].value_counts())

# p = 1, l = 0
# Calculate avg phishing length
# Calculate avg legit length

totalPhishing = 0
totalPhishingLen = 0
totalLegit = 0
totalLegitLen = 0

for i, row in df.iterrows():
    if row["label"] == 1.0:
        totalPhishingLen += len(row["url"])
        totalPhishing += 1
        old_lengths_phishing.append(len(row["url"]))
    else:
        totalLegitLen += len(row["url"])
        totalLegit += 1
        old_lengths_legit.append(len(row["url"]))

avgPhishing = totalPhishingLen / totalPhishing
avgLegit = totalLegitLen / totalLegit

print(avgPhishing)
print(avgLegit)


for i in range(len(old_lengths_legit)):
    print(str(old_lengths_legit[i]) + ",", end="")

print(max(old_lengths_phishing))