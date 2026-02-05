import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("kyc_data.csv")

print("Dataset Loaded Successfully\n")

# -----------------------------
# Duplicate Detection
# -----------------------------
duplicates = df[df.duplicated(subset=["PAN", "Aadhaar"], keep=False)]
print("Duplicate Records:")
print(duplicates)

# -----------------------------
# Missing Values Check
# -----------------------------
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# -----------------------------
# Invalid Age Check
# -----------------------------
invalid_age = df[(df["Age"] < 18) | (df["Age"] > 100)]
print("\nInvalid Age Records:")
print(invalid_age)

# -----------------------------
# Email Validation
# -----------------------------
invalid_email = df[~df["Email"].astype(str).str.contains("@", na=False)]
print("\nInvalid Email Records:")
print(invalid_email)

# -----------------------------
# Summary
# -----------------------------
print("\nData Quality Summary:")
print(f"Total Records: {len(df)}")
print(f"Duplicate Records: {len(duplicates)}")
print(f"Invalid Age Records: {len(invalid_age)}")
