import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import pandas as pd
import csv


def fft_module_individual(filename_read, column_header, color_choice):
    header = ['Freq', 'Amplitude']
    # filename_read = 'FFT_sample.csv'
    # column_header = 'u'
    # color_choice='red'
    data_filename_write = filename_read.split('.')[0] + '_Column_Header_' + column_header + '_FFT_Data.csv'
    image_filename_write = filename_read.split('.')[0] + '_Column_Header_' + column_header + '_FFT_Spectra.jpg'

    df = pd.read_csv(filename_read)
    df.dropna(inplace=True)
    print(column_header)
    u_list = df[column_header].tolist()
    column_to_numpy_array = np.asarray(u_list)
    slice_of_input_array_for_processing_FFT = []

    percentage = float(
        input(
            "Enter the % number of samples for FFT Calculation (default 10 percent). Press Enter to accept default : ") or "10")

    frequency = int(input("Enter the sampling frequency: "))

    # percentage = 10
    # frequency = 100

    N = int(len(u_list) * (percentage / 100))

    # num_samples = 3000
    for i in range(0, N):
        slice_of_input_array_for_processing_FFT.append(column_to_numpy_array[i])

    # frequency of signal
    T = 1 / frequency
    # x=np.linspace(0,N*T,N)#0, ,21
    y = slice_of_input_array_for_processing_FFT
    ####### processs via window  y = windowing(y)
    yf = fft(y)

    xf = np.linspace(0.0, 1.0 / (2 * T), N // 2)  # 0, ,10
    my_list = 2.0 / N * np.abs(yf[0:N // 2])

    with open(data_filename_write, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(i for i in header)
        writer.writerows(zip(xf, my_list))

    plt.clf()
    plt.loglog(xf, 2.0 / N * np.abs(yf[0:N // 2]), color=color_choice)
    plt.grid()
    plt.xlabel('Frequency')
    plt.ylabel('Peaks')
    plt.savefig(image_filename_write)
    # plt.show()
    plt.clf()

filename_read = 'FFT_sample.csv'
column_header = ['u', 'v', 'w']
colors = ["red", "green", "blue"]
for i, j in zip(column_header, colors):
    fft_module_individual(filename_read, i, j)
#

# fft_module_merged(filename_read, column_header, colors)