import numpy as np

from raw_data_pipeline_tools.convert_to_numpy import convert_dat_to_numpy
from raw_data_pipeline_tools.average_signal_fftsize import get_avg_signal
from raw_data_pipeline_tools.preprocessing_plots import create_preprocessing_plots



def preprocessing_pipeline(
    on_signal_filename: str, off_signal_filename: str, fft_size: int, calibration_method: str = "on/off", plot_analysis: bool = True
) -> np.ndarray:
    """
    Take the raw on and off observations, average the signals to create the spectrum and calibrate.

    Args:
        on_signal_filename (str): The on observation filename
        off_signal_filename (str): The off observation filename
        fft_size (int): The size that was used for the fast fourier transformation
        calibration_method (str, optional): The calibration method to be used. (on/off or on-off). Defaults to "on/off".
        plot_analysis (bool, optional): If True then plot the off,on and calibrated spectrum. Defaults to True.
    """
    # Convert the files to numpy arrays
    on_spectrum, off_spectrum = convert_dat_to_numpy(on_signal_filename, off_signal_filename)

    # Average the time series using the fft size
    on_spectrum_avg: np.ndarray = get_avg_signal(on_spectrum, fft_size=fft_size)
    off_spectrum_avg: np.ndarray = get_avg_signal(off_spectrum, fft_size=fft_size)

    # Calibration
    if calibration_method == "on/off":
        calibrated_signal: np.ndarray = on_spectrum_avg / off_spectrum_avg
    elif calibration_method == "on-off":
        calibrated_signal: np.ndarray = on_spectrum_avg - off_spectrum_avg
    else:
        raise ValueError(f"Calibration Method does not exists. : {calibration_method}")
    
    # If we want plots
    if plot_analysis:
        create_preprocessing_plots(on_spectrum_avg, off_spectrum_avg, calibrated_signal, fft_size)

    return calibrated_signal
