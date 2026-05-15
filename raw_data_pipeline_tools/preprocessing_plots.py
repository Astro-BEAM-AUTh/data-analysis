import matplotlib.pyplot as plt
import numpy as np


def create_preprocessing_plots(on_spectrum_avg: np.ndarray, off_spectrum_avg: np.ndarray, calibrated_signal: np.ndarray, fft_size: int) -> None:
    """
    Create on_spectrum , off_spectrum , calibrated_spectrum plots in frequencies axes.

    Args:
        on_spectrum_avg (np.ndarray): the on spectrum
        off_spectrum_avg (np.ndarray): the off spectrum
        calibrated_signal (np.ndarray): the calibrated spectrum
        fft_size (int): the fft size used in the observation
    """
    frequencies = np.linspace(1.4205 - 0.003840 / 2, 1.4205000 + 0.003840 / 2, fft_size)

    _, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(8, 10))

    ax1.plot(frequencies, off_spectrum_avg, color="blue")
    ax1.set_title("Avg Cold/Off")
    ax1.set_ylabel("Relative Power")

    ax2.plot(frequencies, on_spectrum_avg, color="red")
    ax2.set_title("Avg Hot/On")
    ax2.set_ylabel("Relative Power")

    ax3.plot(frequencies, calibrated_signal, color="green")
    ax3.set_title("On/Off calibration")
    ax3.set_ylabel("Relative Power")
    ax3.set_xlabel("Frequencies")
    plt.tight_layout()
    plt.show()
