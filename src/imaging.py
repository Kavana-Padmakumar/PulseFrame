import numpy as np
import pywt
from pyts.image import GramianAngularField, RecurrencePlot

def to_gaf(window):
    gaf = GramianAngularField(image_size=window.shape[0], method='summation')
    return gaf.fit_transform(window.reshape(1, -1))[0]

def to_rp(window):
    rp = RecurrencePlot(threshold='point', percentage=20)
    return rp.fit_transform(window.reshape(1, -1))[0]

def to_cwt(window, scales=np.arange(1, 128), wavelet='morl'):
    coefficients, _ = pywt.cwt(window, scales, wavelet)
    return coefficients

def process_subject(signal, window_size, step_size):
    windows = make_windows(signal, window_size, step_size)
    gaf_imgs = [to_gaf(w) for w in windows]
    rp_imgs = [to_rp(w) for w in windows]
    cwt_imgs = [to_cwt(w) for w in windows]
    return np.array(gaf_imgs), np.array(rp_imgs), np.array(cwt_imgs)
