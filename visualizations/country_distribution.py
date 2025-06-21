import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_country_distribution(df):
    top_countries = df['country'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette="Set2")
    plt.title("Top 10 Countries on Netflix")
    plt.xlabel("Number of Titles")
    plt.ylabel("Country")
    plt.tight_layout()

    # Save figure
    os.makedirs("screenshots", exist_ok=True)
    plt.savefig("screenshots/full_country_distribution.png")
    plt.show()
