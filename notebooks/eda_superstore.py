import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/superstore.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== DATASET INFO ==========")
print(df.info())
