import numpy as np


def get_avg_signal(time_series: np.ndarray, fft_size: int) -> np.ndarray:
    """
    Create the average spectrum from the time series.

    Args:
       time_series (np.ndarray): The time series to be averaged
       fft_size (int): The size that was used for the fast fourier transformation
    Returns:
       np.ndarray: The average spectrum
    """
    if fft_size <= 0:
        msg = "fft_size must be a positive integer"
        raise ValueError(msg)

    usable_size = (time_series.size // fft_size) * fft_size

    if usable_size == 0:
        msg = "time_series must contain at least one complete fft_size block"
        raise ValueError(msg)

    trimmed = time_series[:usable_size]
    reshaped = trimmed.reshape(-1, fft_size)
    return reshaped.mean(axis=0)
