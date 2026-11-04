import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/processed/2014_data_cleaned.csv", encoding="latin1", low_memory=False, on_bad_lines="skip")

old_lengths_phishing = []
old_lengths_legit = []

totalOldPhishing = 0
totalOldPhishingLen = 0
totalOldLegit = 0
totalOldLegitLen = 0

for i, row in df.iterrows():
    if row["label"] == 1.0:
        totalOldPhishingLen += int(row["url_len"])
        totalOldPhishing += 1
        old_lengths_phishing.append(int(row["url_len"]))
    else:
        totalOldLegitLen += int(row["url_len"])
        totalOldLegit += 1
        old_lengths_legit.append(int(row["url_len"]))

avgOldPhishing = totalOldPhishingLen / totalOldPhishing
avgOldLegit = totalOldLegitLen / totalOldLegit

df2 = pd.read_csv("data/processed/2026_data_cleaned.csv", encoding="latin1", low_memory=False, on_bad_lines="skip")

new_lengths_phishing = []
new_lengths_legit = []

totalPhishing = 0
totalPhishingLen = 0
totalLegit = 0
totalLegitLen = 0

for i, row in df2.iterrows():
    if row["label"] == 1.0:
        totalPhishingLen += int(row["url_len"])
        totalPhishing += 1
        new_lengths_phishing.append(int(row["url_len"]))
    else:
        totalLegitLen += int(row["url_len"])
        totalLegit += 1
        new_lengths_legit.append(int(row["url_len"]))

avgPhishing = totalPhishingLen / totalPhishing
avgLegit = totalLegitLen / totalLegit

# print(avgPhishing)
# print(avgLegit)


# for i in range(len(old_lengths_legit)):
#     print(str(old_lengths_legit[i]) + ",", end="")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8,5))


# 2014
ax[0].hist(old_lengths_phishing, bins=10, range=(0,360), alpha=0.6, label="Phishing", color="red")
ax[0].hist(old_lengths_legit, bins=10, range=(0,360), alpha=0.6, label="Legitimate", color="blue")

# Draw means
ax[0].axvline(avgOldPhishing, color="red", linestyle="--")
ax[0].axvline(avgOldLegit, color="blue", alpha=0.6, linestyle="--")

ax[0].set_title("Phishing vs. Legitimate URL Lengths (2014 Dataset)")
ax[0].set_xlabel("URL Length (characters)")
ax[0].set_ylabel("Frequency")

# 2026
ax[1].hist(new_lengths_phishing, bins=10, range=(0,360), alpha=0.6, label="Phishing", color="red")
ax[1].hist(new_lengths_legit, bins=10, range=(0,360), alpha=0.6, label="Legitimate", color="blue")

# Draw means
ax[1].axvline(avgPhishing, color="red", linestyle="--")
ax[1].axvline(avgLegit, color="blue", alpha=0.6, linestyle="--")

ax[1].set_title("Phishing vs. Legitimate URL Lengths (2026 Dataset)")
ax[1].set_xlabel("URL Length (characters)")
ax[1].set_ylabel("Frequency")

ax[0].legend(loc="upper right")
ax[1].legend(loc="upper right")


plt.show()