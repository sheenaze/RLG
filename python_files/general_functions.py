import math as mt
import numpy as np
from general_classes import *


def validate_coordinates(angle):
    return 0 <= angle <= 2 * mt.pi


def deg2rad(angle):
    '''
    Remark: works for both scalar values and matrices
    :param arc_seconds: angle in degrees
    :return: angle in radians
    '''
    return angle * np.pi / 180

def as2rad(arc_seconds):
    '''
    Remark: works for both scalar values and matrices
    :param arc_seconds: angle in arcseconds
    :return: angle in radians
    '''
    return arc_seconds * np.pi / 180 / 3600

def degrees_to_dms(degrees):
    '''
    Remark: works for both scalar values and matrices
    :param degrees: angle given in degrees with decimal part
    :return: angle given in format: [degrees minutes seconds]
    '''
    deg_floored = np.floor(degrees)
    minutes = (degrees - deg_floored) * 60
    min_floored = np.floor(minutes)
    seconds = np.round((minutes - min_floored) * 60, 5)
    return np.vstack((deg_floored, min_floored, seconds)).T


def n_radius(fi, a_axis=GRS80.a_axis, e2=GRS80.e2):
    '''
    Remark: works for both scalar values and matrices
    :param fi: latitude
    :param a_axis: semimajor axis of an ellipsoid (GRS80 by default)
    :param e2:  first eccentricity
    :return:  the prime vertical radius of curvature
    '''
    nominator = a_axis
    denominator = np.sqrt(1 - e2 * (np.sin(fi)) ** 2)
    return np.divide(nominator, denominator)


def m_radius(fi, a_axis=GRS80.a_axis, e2=GRS80.e2):
    '''
    Remark: works for both scalar values and matrices
    :param fi: latitude
    :param a_axis: semimajor axis of an ellipsoid (GRS80 by default)
    :param e2:  first eccentricity
    :return:  the meridian radius of curvature
    '''
    nominator = a_axis * (1 - e2)
    denominator = (np.sqrt(1 - e2 * (np.sin(fi)) ** 2)) ** 3
    return np.divide(nominator, denominator)


# ================== Testing part ====================
if __name__ == '__main__':
    print('Hello')
    matrix = np.arange(50)+np.arange(50)/60+np.arange(50)/3600
    print(degrees_to_dms(50+50/60+30/3600))
    dms = degrees_to_dms(50+50/60+30/3600)
    # dms = degrees_to_dms(matrix)
    print(dms, dms.shape)
    # n = n_radius(matrix)
    # print(n.shape)
    # print(n_radius(matrix))
    # print(n_radius(0))
    # print(m_radius(matrix))




