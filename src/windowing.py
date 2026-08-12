import numpy as np

def make_windows(signal, window_size, step_size):
    windows = []
    for start in range(0, len(signal) - window_size + 1, step_size):
        windows.append(signal[start:start + window_size])
    return np.array(windows)
