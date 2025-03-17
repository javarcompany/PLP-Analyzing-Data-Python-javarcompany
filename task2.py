import pandas as pd

# -------Step 1: Basic Statistics
df = pd.read_csv('IMDb 2024 Movies TV Shows.csv')

# Basic statistics of the numerical columns
print(df.describe())

# ------Step 2: Grouping by a Categorical Column
# Group by 'type' (Movie/TV Show) and calculate the mean rating
grouped = df.groupby('type')['rating'].mean()
print(grouped)

# Print the result
print("\nGrouped Stats by Type (Movie vs TV Show):\n", grouped)

# Group by 'genre' and calculate the mean rating for each genre
grouped_genre_stats = pd.groupby('genre')['rating'].mean()

# Print the result
print("\nGrouped Stats by Genre:\n", grouped_genre_stats)

# Identify the maximum and minimum average ratings by genre
max_rating_genre = grouped_genre_stats.idxmax()  # Genre with the highest average rating
min_rating_genre = grouped_genre_stats.idxmin()  # Genre with the lowest average rating

print(f"Genre with Highest Average Rating: {max_rating_genre}")
print(f"Genre with Lowest Average Rating: {min_rating_genre}")

# Check for missing values in the dataset
missing_data = pd.isnull().sum()

# Print columns with missing data
print("Missing Data:\n", missing_data)
