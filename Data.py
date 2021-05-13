import numpy as np
from numpy import asarray

def find_nearest(array, value):
    """
    Finds Nearest Value to input value in array
    Parameters
    ----------
    array : array
        Array in which value is being found
    value : float
        Value that is being found
    Returns
    ----------
    array[idx] : float
        Nearest Value to value
    '"""
    array = asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def expand(x_array,y_array,new_length):                                        
    """"
    Expands y_array by a factor of the variable "scale" 
        
    """
    new_array = np.zeros(new_length)
    x = np.linspace(x_array[0],x_array[-1],num=new_length)
    new_array = np.interp(x,x_array,y_array)
    return new_array
