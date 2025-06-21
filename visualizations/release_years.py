# visualizations/release_years.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_release_trend(df):
    """Shows release year distribution."""
    plt.figure(figsize=(12,6))
    sns.histplot(data=df, x='release_year', bins=30, kde=True, color="coral")
    plt.title("Content Release Trend on Netflix")
    plt.xlabel("Release Year")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
