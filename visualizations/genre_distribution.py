import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_genre_distribution(df):
    genres = df['listed_in'].str.split(', ', expand=True).stack()
    top_genres = genres.value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(y=top_genres.index, x=top_genres.values, palette="viridis")
    plt.title("Top 10 Genres on Netflix")
    plt.xlabel("Number of Shows")
    plt.ylabel("Genre")
    plt.tight_layout()

    # Save figure
    os.makedirs("screenshots", exist_ok=True)
    plt.savefig("screenshots/full_genre_distribution.png")
    plt.show()
