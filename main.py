import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.data_loader import load_data
from utils.preprocessing import clean_data
from visualizations.genre_distribution import plot_genre_distribution
from visualizations.release_years import plot_release_trend
from visualizations.country_distribution import plot_country_distribution

def main():
    path = "data/netflix_titles_sample.csv"
    df = load_data(path)
    df_clean = clean_data(df)

    plot_genre_distribution(df_clean)
    plot_release_trend(df_clean)
    plot_country_distribution(df_clean)

if __name__ == "__main__":
    main()
