import pandas as pd

def load_excel(filepath):
    """Load a single Excel file as a Pandas DataFrame."""
    try:
        return pd.read_excel(filepath)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None

def load_all_data(file_paths):
    """Load all Excel files and return a dictionary of Pandas DataFrames."""
    data_frames = {}
    for key, path in file_paths.items():
        data_frames[key] = load_excel(path)
    return data_frames
