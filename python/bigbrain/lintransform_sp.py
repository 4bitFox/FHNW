#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:34:42 2025

@author: cvetkofabian
"""

import sympy as sp

def hduplicate(vec, n):
    M = vec * sp.ones(1, n)
    return M

def coeff_matrix(P, Q):
    A = Q*P.inv()
    return A

def transform(P, A, b = sp.zeros(2, 1)):
    Q = A * P + b
    return Q
    
def fixed_point(A, b):
    eye = sp.eye(A.shape[0])
    eyeA = eye - A
    eyeAb = eyeA.row_join(b)
    det = eyeA.det()
    if det != 0:
        x_F = eyeA.inv() * b
        return x_F
    elif eyeA.rank() != eyeAb.rank():
        print("Existiert kein x_F!!!")
        return None
    else:
        print("Exisiteren unendlich x_F!!!")
        return eyeAb.rref()[0]

def rotatation_matrix(angle):
    s = sp.sin(angle)
    c = sp.cos(angle)
    rot_M = sp.Matrix([[c, -s], [s, c]])
    return rot_M

def rotate_2D(M, angle, rotation_point = sp.zeros(2, 1)):
    M_amount_vectors = M.shape[1]
    if M_amount_vectors != 1: # broadcast if matrix with hstacked vectors
        rotation_point = hduplicate(rotation_point, M_amount_vectors)
    rotated = rotatation_matrix(angle) * (M - rotation_point) + rotation_point
    return rotated
