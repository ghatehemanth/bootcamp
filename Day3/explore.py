import pandas as pd

df = pd.read_csv("vendor_payments.csv")

print("Shape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset preview:")
print(df.head())