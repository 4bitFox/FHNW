#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:34:42 2025

@author: cvetkofabian
"""

import sympy as sp

def hduplicate(vec, n):
    """
    returns matrix with vector repeated horizontally n times.
    """
    if vec.shape[1] != 1:
        raise ValueError("vec has to be a column vector!")
    M = vec * sp.ones(1, n)
    return M

def coeff_matrix(P, Q):
    """
    Returns the coefficeint matrix of P -> Q
    Derived from Q = A*P
    """
    A = Q*P.inv()
    return A

def transform(P, A, b = sp.zeros(2, 1)):
    """
    Transform P with A and b to Q
    Q = A*P+b
    """
    Q = A * P + b
    return Q
    
def fixed_point(A, b):
    """
    Try to find a fixed point
    """
    eye = sp.eye(A.shape[0])
    eyeA = eye - A
    eyeAb = eyeA.row_join(b)
    det = eyeA.det()
    if det != 0:
        x_F = eyeA.inv() * b
        return x_F
    elif eyeA.rank() != eyeAb.rank():
        print("No fixed point x_F exists!")
        return None
    else:
        print("Infinite fixed points x_F exist!")
        return eyeAb.rref()[0]

def rotation_matrix(angle, axis = None):
    """
    Calculate the rotation matrix with a given angle
    if axis is not defined, 2 dimensions are assumed
    if axis is defined as x, y, z, the matrix will be 3-dimensional
    """
    s = sp.sin(angle)
    c = sp.cos(angle)
    if axis == None: # 2D
        rot_M = sp.Matrix([[c, -s], 
                           [s,  c]])
    elif axis == "z": # 3D around z
        rot_M = sp.Matrix([[ c, -s,  0], 
                           [ s,  c,  0], 
                           [ 0,  0,  1]])
    elif axis == "x": # 3D around x
        rot_M = sp.Matrix([[ 1,  0,  0], 
                           [ 0,  c, -s], 
                           [ 0,  s,  c]])
    elif axis == "y": # 3D around y
        rot_M = sp.Matrix([[ c,  0,  s], 
                           [ 0,  1,  0], 
                           [-s,  0,  c]])
    else:
        raise ValueError("axis has to be NoneType (default), 'x', 'y' or 'z'!")
    return rot_M

def rotate(M, angle, rotation_point = None, axis = None):
    """
    rotate M at with a given angle. 
    If a rotation point is given, M will be rotated around it.
    If axis isn't specified, M is assumed to be 2D. Otherwise rotation will take place around the specified axis x, y, or z and M is assumed to be 3D.
    """
    if rotation_point == None:
        rotation_point = sp.zeros(M.shape[0], 1)
    M_amount_vectors = M.shape[1]
    if M_amount_vectors != 1: # broadcast if matrix with hstacked vectors
        rotation_point = hduplicate(rotation_point, M_amount_vectors)
    rotated = rotation_matrix(angle, axis) * (M - rotation_point) + rotation_point
    return rotated
