import numpy as np

def get_avg_signal(time_series, fft_size):
    """
    Create the average spectrum from the time series.
    """

    if fft_size <= 0:
         raise ValueError("fft_size must be a positive integer")
    usable_size = (time_series.size // fft_size) * fft_size
    if usable_size == 0:
         raise ValueError("time_series must contain at least one complete fft_size block")
    trimmed = time_series[:usable_size]
    reshaped = trimmed.reshape(-1, fft_size)
    return reshaped.mean(axis=0)