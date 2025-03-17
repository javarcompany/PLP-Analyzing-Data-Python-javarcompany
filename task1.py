import pandas as pd

# -----Step 1: Load the Dataset
# Load the Iris dataset
df = pd.read_csv('IMDb 2024 Movies TV Shows.csv')

# Display the first few rows of the dataset
print(df.head())

# -----Step 2: Inspect the Data
# Check the data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

# ----Step 3: Clean the Dataset
# Option 1: Dropping missing values
df_cleaned = df.dropna()

def remove_dollar(value):
    if "$" in value:
        return value.replace("$", "")

def remove_comma(value):
    if "," in value:
        return value.replace(",", "")
    
def convert_shorthand(value):
    # Check if the value contains 'K' (thousands)
    if 'K' in value:
        return float(value.replace('K', '')) * 1000
    # Check if the value contains 'M' (millions)
    elif 'M' in value:
        return float(value.replace('M', '')) * 1000000
    # Check if the value contains 'B' (billions)
    elif 'B' in value:
        return float(value.replace('B', '')) * 1000000000
    # If no abbreviation is present, return the value as float
    else:
        return float(value)
    
    
# Option 2: Removing Revenue Symbol and comma the converting it to numeric type
df['Revenue'] = df['Revenue'].apply(remove_dollar)
df['Revenue'] = df['Revenue'].apply(remove_comma)
df['Revenue'] = df['Revenue'].apply(convert_shorthand)
print(df['Revenue'])

# Replace (K) to (000) in Vote_Count
df['Vote_Count'] = df['Vote_Count'].apply(remove_comma)
df['Vote_Count'] = df['Vote_Count'].apply(convert_shorthand)
print(df['Vote_Count'])

# Clean Budget Column
df["Budget"] = df['Budget'].apply(remove_comma)
df['Budget'] = df['Budget'].apply(remove_dollar)
print(df["Budget"].value_counts())