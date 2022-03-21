def bpfilt(x,dt,lf,hf):
    """
    BPFILT Bandpass filter time series.
    BPFILT(X,DT,LF,HF) takes a time series sampled at DT
    and filters it with a 2nd order, two-pass butterworth
    filter between frequencies LF and HF. If X is a matrix
    BPFILT filters the individual rows of X.
    """
    import numpy as np
    from scipy.signal import butter
    from scipy.signal import filtfilt

    nyq=0.5/dt
    wn=np.array([lf/nyq, hf/nyq])
    [b,a]=butter(2,wn,'bandpass')
    y=filtfilt(b,a,x,axis=0)

    return y
