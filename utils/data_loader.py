# utils/data_loader.py
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Loads Netflix dataset from CSV."""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()
