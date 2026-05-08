import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import functions from folder
from raw_data_pipeline_tools.data_convert_to_csv import dat_to_csv
from raw_data_pipeline_tools.average_signal_fftsize import get_avg_signal

def main():

    # If we want to do calibration then set this to True
    calibration = True

    # The fft size defined from the observation
    fft_size = 2048

    frequencies = np.linspace(1.4205 - 0.003840/2, 1.4205000 + 0.003840/2, fft_size)

    on_observation_filename = '2502202_Hot202020.csv'
    off_observation_filename = "2502202_Cold202020.csv"

    # Files Management
    if on_observation_filename.endswith(".dat"):
        base_name = on_observation_filename.split('.')[0]
        on_observation_filename = f"{base_name}.csv"
        dat_to_csv(f"{base_name}.dat", on_observation_filename)
        
    if off_observation_filename.endswith(".dat"):
        base_name = off_observation_filename.split('.')[0]
        off_observation_filename = f"{base_name}.csv"
        dat_to_csv(f"{base_name}.dat", off_observation_filename)

    # ON signal proccesing
    on_series_df = pd.read_csv(on_observation_filename)
    on_series_df = on_series_df.filter(regex='power_au|y_axis')
    on_series_np = on_series_df.to_numpy()
    
    avg_on = on_series_np
    if len(on_series_np) > fft_size:
        avg_on = get_avg_signal(on_series_np, fft_size)

    # Check for Calibration & Plotting
    if calibration:
        off_series_df = pd.read_csv(off_observation_filename)
        off_series_df = off_series_df.filter(regex='power_au|y_axis')
        off_series_np = off_series_df.to_numpy()
        
        avg_off = off_series_np
        if len(off_series_np) > fft_size:
            avg_off = get_avg_signal(off_series_np, fft_size)
            
        calibrated_signal = avg_on / avg_off

        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(8, 10))

        ax1.plot(frequencies, avg_off, color='blue')
        ax1.set_title('Avg Cold/Off')
        ax1.set_ylabel('Relative Power')

        ax2.plot(frequencies, avg_on, color='red')
        ax2.set_title('Avg Hot/On')
        ax2.set_ylabel('Relative Power')

        ax3.plot(frequencies, calibrated_signal, color='green')
        ax3.set_title('On/Off calibration')
        ax3.set_ylabel('Relative Power')
        ax3.set_xlabel('Frequencies')
        plt.tight_layout()
        plt.show()
    else:
        plt.plot(frequencies, avg_on, color='blue')
        plt.title('Target signal')
        plt.ylabel('Relative Power')
        plt.xlabel('Frequencies')
        plt.show()

if __name__ == "__main__":
    main()