import numpy as np
import os

def convert_dat_to_numpy(on_file_path: str, off_file_path : str):
    """
    Convert .dat files to numpy arrays
    """
    try:
        on_signal_numpy = np.fromfile(on_file_path, dtype=np.float32)
        off_signal_numpy = np.fromfile(off_file_path, dtype=np.float32)
        
        return on_signal_numpy, off_signal_numpy
    except FileNotFoundError:
        print(f"File not found")
    except Exception as e:
        print(f"Convert Error: {e}")
