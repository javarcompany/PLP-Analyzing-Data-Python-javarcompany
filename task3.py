import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('IMDb 2024 Movies TV Shows.csv')

# Plot the distribution of ratings for movies and TV shows
sns.boxplot(data=df, x='type', y='rating')
plt.title('Rating Distribution by Type (Movie vs TV Show)')
plt.show()

grouped_genre_stats = pd.groupby('genre')['rating'].mean()

# Plot the average rating by genre
grouped_genre_stats.plot(kind='bar', figsize=(10, 6))
plt.title('Average Rating by Genre')
plt.ylabel('Average Rating')
plt.show()
