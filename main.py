# Import functions from folder
from raw_data_pipeline_tools.preprocessing_pipeline import preprocessing_pipeline


def main() -> None:
    on_filename = "/home/dimitrios-pakakis/Desktop/Astro/data-analysis/2502202_Hot202020.dat"
    off_filename = "/home/dimitrios-pakakis/Desktop/Astro/data-analysis/2502202_Cold202020.dat"
    fft_size = 2048
    _ = preprocessing_pipeline(
        on_signal_filename=on_filename, off_signal_filename=off_filename, fft_size=fft_size, calibration_method="on/off", plot_analysis=True
    )


if __name__ == "__main__":
    main()
