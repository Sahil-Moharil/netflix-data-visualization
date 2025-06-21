# utils/preprocessing.py

def clean_data(df):
    """Performs basic cleaning like handling nulls."""
    df = df.copy()
    df.dropna(subset=["type", "title", "country", "release_year", "listed_in"], inplace=True)
    return df
