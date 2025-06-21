import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_release_trend(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='release_year', bins=30, kde=True, color="coral")
    plt.title("Content Release Trend on Netflix")
    plt.xlabel("Release Year")
    plt.ylabel("Count")
    plt.tight_layout()

    # Save figure
    os.makedirs("screenshots", exist_ok=True)
    plt.savefig("screenshots/full_release_trend.png")
    plt.show()
