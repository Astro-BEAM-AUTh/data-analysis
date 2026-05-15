import numpy as np


def convert_dat_to_numpy(on_file_path: str, off_file_path: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert .dat files to numpy arrays.

    Args:
        on_file_path (str): The file path of the on observation .dat file.
        off_file_path (str): The file path of the off observation .dat file.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple containing the on and off signal as numpy arrays.
    """
    try:
        on_signal_numpy = np.fromfile(on_file_path, dtype=np.float32)
        off_signal_numpy = np.fromfile(off_file_path, dtype=np.float32)

    except FileNotFoundError:
        print("File not found")  # noqa: T201
    except Exception as e:  # noqa: BLE001
        print(f"Convert Error: {e}")  # noqa: T201
    else:
        return on_signal_numpy, off_signal_numpy
