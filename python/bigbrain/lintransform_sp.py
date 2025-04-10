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

def hsplit(M):
    """
    split M into column vectors
    """
    vectors = []
    for vector_index in range(M.shape[1]):
        components = []
        for row in range(M.shape[0]):
            components.append(M[row, vector_index])
        vector = sp.Matrix([components]).T
        vectors.append(vector)
    return tuple(vectors)

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
    if axis is a vector, the vector will become the rotation axis
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
        p = axis
        r, theta, phi = carthesian_to_spherical_coordinates(p)
        R_Z = rotation_matrix(phi, "z")
        R_Y = rotation_matrix(theta, "y")
        rot_M = R_Z * R_Y * rotation_matrix(angle, "z") * R_Y.T * R_Z.T
    return rot_M

def rotate(M, angle, rotation_point = None, axis = None):
    """
    rotate M with a given angle. 
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

def mirror_matrix(angle = 0, slope = None, plane_n = None):
    """
    Calculate mirror matrix with given angle, slope or normal vector of plane.
    """
    
    if slope != None:
        m = slope
        mirror_M = 1/(1+m**2) * sp.Matrix([[1-m**2, 2*m], [2*m, m**2-1]])
    elif plane_n != None:
        n = plane_n
        mirror_M = sp.eye(3) - ((2*n*n.T) / n.norm()**2) #####################NOT_TESTED###########################
    else:
        s = sp.sin(2*angle)
        c = sp.cos(2*angle)
        mirror_M = sp.Matrix([[c,  s], 
                              [s, -c]])
    return mirror_M

def mirror_2D(M, angle = 0, slope = None):
    """
    Mirror M around a line with angle relative to the X-axis.
    If angle is not defined (angle=0), it will mirror around X-axis.
    """
    if slope == None:
        mirror_M = mirror_matrix(angle = angle)
    else:
        mirror_M = mirror_matrix(slope = slope)
    
    M_mirrored = mirror_M * M
    return M_mirrored

def mirror_3D(M, n): #####################NOT_TESTED###########################
    """
    Mirror M with a plane normal.
    """
    mirror_M = mirror_matrix(plane_n = n)
    M_mirrored = mirror_M * M
    return M_mirrored

def carthesian_to_spherical_coordinates(p):
    """
    Takes a vector p and returns r, theta and phi as a tuple
    """
    r = p.norm()
    theta = sp.acos(p[2]/r)
    phi = sp.atan(p[1]/p[0])
    return r, theta, phi

def sperical_to_carthesian_coordinates(r, theta, phi):
    """
    Takes r, tetha and phi and turns them into a carthesian vector
    """
    x = r*sp.sin(theta)*sp.cos(phi)
    y = r*sp.sin(theta)*sp.sin(phi)
    z = r*sp.cos(theta)
    p = sp.Matrix([[x, y, z]]).T
    return p
