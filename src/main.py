from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

df = pd.read_csv("data/processed/2014_data_cleaned.csv", encoding="latin1", low_memory=False, on_bad_lines="skip")

x = df["url"]
y = df["label"]

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=67)

# Create and train model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Predict based off test data
Y_prediction = model.predict(X_test)

# Evaluate accuracy
acc = accuracy_score(Y_test, Y_prediction)
print("Accuracy: ", acc)
