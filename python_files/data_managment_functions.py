import math as mt
import numpy as np
from general_classes import *
from scipy.io import loadmat
from general_functions import *
from astropy.time import Time


def window_averaging(data, window, mjd, full_hours=True):
    """


    Parameters
    ----------
    data : column array
        equaly sampled data to be averaged
    window : int
        number of epochs to be averaged
        (eg. if the data samplig frequency is 1 per second and we want to have data with 1
         hour resolution, then the window is 3600)
    mjd : column array
        epoch array given in mjd
    full_hours : bool, optional
        if true data is averaged starting from the next full hour,
        if not then with the first given epoch and then for every
        +window epoch. The default is True.

    Returns
    -------
    None.

    """
    mjd = Time(mjd, format='mjd')
    if full_hours:
        # mjd - floor(mjd) gives hours in mjd scale,
        # dividing by 1/24 gives number of hours since the initial epoch
        # modf returns integral and fractional parts
        hours = np.round(np.modf(mjd.value)[0] * 24, 8)

        full_hours_ind = np.where(hours - np.floor(hours) == 0)[0]
        first_full_hour_ind = full_hours_ind[np.where(
            full_hours_ind >= window / 2)[0][0]]

        if window % 2 == 0:
            ind = int(first_full_hour_ind - window / 2)
            dist_to_next_ind = int(window / 2)
        else:
            ind = int(first_full_hour_ind - window / 2 - 0.5)
            dist_to_next_ind = int(window / 2 + 0.5)

        new_data = data[ind:]
        MJD = mjd.value[ind:]

        length = new_data.shape[0]
        residuum = length % window
        length_of_new_series = int((length - residuum) / window)

        MJD = MJD[0:length - residuum].reshape((length_of_new_series, window)).T
        MJD = MJD[dist_to_next_ind, :].reshape(length_of_new_series, 1)

        new_data = new_data[0:length - residuum].reshape((length_of_new_series, window)).T

    else:
        length = data.shape[0]
        residuum = length % window
        length_of_new_series = int((length - residuum) / window)

        MJD = mjd.value[0:length - residuum].reshape((length_of_new_series, window)).T
        MJD = MJD.mean(axis=0).reshape(length_of_new_series, 1)

        new_data = data[0:length - residuum].reshape((length_of_new_series, window)).T

    average_data = new_data.mean(axis=0).reshape(length_of_new_series, 1)
    data_std = new_data.std(axis=0, ddof=1).reshape(length_of_new_series, 1)
    return np.concatenate((MJD, average_data, data_std), axis=1)
