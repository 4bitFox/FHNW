#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import numpy as np


def vector(components):
    """
    Turn list into vector

    Parameters
    ----------
    components : list
        1D List containing vector components

    Returns
    -------
    vector : ndarray
        Vector as numpy array.

    """
    vector = np.array([components]).T
    return vector


def angle(vec1, vec2):
    """
    Get angle between two vectors

    Parameters
    ----------
    vec1 : TYPE
        DESCRIPTION.
    vec2 : TYPE
        DESCRIPTION.

    Returns
    -------
    angle : Angle in radian

    """
    angle = np.arccos(np.vdot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
    return(angle)


def spurpunkte(p_0, u):
    """
    Erhalte die Spurpunkte einer Geraden

    Parameters
    ----------
    p_0 : TYPE
        DESCRIPTION.
    u : TYPE
        DESCRIPTION.

    Returns
    -------
    points : Spurpunkte in einem dict.

    """
    if np.shape(p_0) != np.shape(u):
        raise Exception("p_0 und u haben nicht die gleichen dimensionen")
    if np.shape(p_0)[0] > 3:
        raise Exception("Zu hohe dimension. Max: 3D")
        
    t = -p_0 / u
    solution = p_0 + u@t.T
    
    axes = "xyz"
    points = {}
    for i in range(np.shape(p_0)[0]):
        plane = ""
        intersection_in_plane = []
        for j in range(np.shape(p_0)[0]):
            if not j == i:
                plane = plane + axes[j]
            intersection_in_plane.append(solution[j][i])   
        intersection_in_plane = np.array([intersection_in_plane]).T
        points[plane] = intersection_in_plane
    return points
