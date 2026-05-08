import numpy as np

def get_avg_signal(time_series, fft_size):
    """
    Create the average spectrum from the time series.
    """
    reshaped = time_series.reshape(-1, fft_size)
    return reshaped.mean(axis=0)