import os
import pickle
import numpy as np

def load_subject_data(file_path):
    """
    Loads WESAD/PPG-DaLiA subject data safely.
    Returns data dictionary if found, otherwise logs a warning and returns None.
    """
    if not os.path.exists(file_path):
        print(f"[WARNING] Subject file not found: {file_path}. Skipping...")
        return None
        
    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f, encoding='latin1')
        print(f"[SUCCESS] Loaded dataset from {file_path}")
        return data
    except Exception as e:
        print(f"[ERROR] Failed to load {file_path}: {e}")
        return None
