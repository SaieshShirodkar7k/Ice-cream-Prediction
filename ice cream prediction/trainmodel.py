import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Clean data (remove bad rows like '124a')
df = df[pd.to_numeric(df["IceCreamsSold"], errors="coerce").notnull()]
df["IceCreamsSold"] = df["IceCreamsSold"].astype(int)

# Features: Temperature, Rainfall
X = df[["Temperature", "Rainfall"]]
y = df["IceCreamsSold"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
print("Model trained and saved as model.pkl")
