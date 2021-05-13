import numpy as np

def rms(array):                                                                
    """
    Returns the root mean squred for an array of values
    Parameters
    ----------
    array : narray
        Array of values from which the RMS is calculated
    Returns
    ----------
    rms : float
        The rms of the data
    """
    rms = np.sqrt(np.mean(array**2))
    return rms