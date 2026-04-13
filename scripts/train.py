import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("dataset/winequality.csv")

X = df.drop("quality", axis=1)
y = df["quality"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model saved! Yayyyyy")