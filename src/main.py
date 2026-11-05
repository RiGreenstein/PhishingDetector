from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

import pandas as pd

df = pd.read_csv("data/processed/2014_data_cleaned.csv", encoding="latin1", low_memory=False)

x = df["url"]
y = df["label"]

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=67, stratify=y)

text_model = make_pipeline(
   TfidfVectorizer(analyzer="char", ngram_range=(3, 5), min_df=2),
   LogisticRegression(max_iter=1000),
)

text_model.fit(X_train, Y_train)

prediction = text_model.predict(X_test)

print("Training URLs: ", len(X_train))
print("Test URLs: ", len(X_test))

print(f"Accuracy: {accuracy_score(Y_test, prediction):.3f}")

print("\nClassification report:")

print(classification_report(Y_test, prediction, labels=[0, 1], target_names=["Legitimate", "Phishing"], zero_division=0))

tn, fp, fn, tp = confusion_matrix(Y_test, prediction, labels=[0, 1]).ravel()

print("Confusion matrix:")
print(f"  Correctly identified legitimate: {tn}")
print(f"  Inorrectly identified legitimate: {fp}")
print(f"  Incorrectly identified phishing: {fn}")
print(f"  Correctly identified phishing: {tp}")

if tn + fp > 0:
    false_positive_rate = fp / (tn + fp)
    print(f"\nFalse positive rate: {false_positive_rate:.3f}")
