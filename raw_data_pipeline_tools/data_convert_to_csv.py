import csv
import numpy as np

def dat_to_csv(filename, csv_filename):
    """
    Convert .dat file to csv file.

    Args:
        filename (str): the .dat file to be converted
        csv_filename (str): the name for the csv file
    """
    y_data_list = np.fromfile(filename, dtype=np.float32)

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['y_axis'])
        rows = zip(y_data_list)
        writer.writerows(rows)