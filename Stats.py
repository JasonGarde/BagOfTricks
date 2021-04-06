import numpy as np

def rms(array):                                                                
    """Returns the root mean squred for an array of values"""
    return np.sqrt(np.mean(array**2))