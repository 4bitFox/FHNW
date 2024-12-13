#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:46:01 2024

@author: cvetkofabian
"""

import sympy as sp

def symbols_real(symbols):
    """
    Create a sympy symbol for real numbers
    """
    return sp.symbols(symbols, real=True)

def vec(components):
    """
    Create a vector in vertical format
    """
    vector = sp.Matrix([components]).T
    return vector

def line(p_0, u, t=symbols_real("t")):
    """
    Create a line p_0 + t+u
    returns line and t-symbol
    """
    g = p_0 + t*u
    return g, t

def angle(vec1, vec2):
    angle = sp.acos(vec1.dot(vec2) / (vec1.norm() * vec2.norm()))
    return angle

def in_plane(n, p_0, p):
    CrossP = n.cross(p_0 - p)
    if CrossP.norm() == 0:
        print(p, "liegt in der Ebene p_0", p_0, "n", n)
        return True
    else:
        print(p, "liegt NICHT in der Ebene p_0:", p_0, "n:", n, "\n CrossP.norm():", CrossP.norm())
        return False
    
def plane_D2p_0(n, D, axis="x"):
    """
    Convert D from coordinate plane to p_0 for plane using normal vector
    """
    x = n[0]
    y = n[1]
    z = n[2]
    if axis == "x":
        p_0 = vec([-D/x, 0, 0])
    elif axis == "y":
        p_0 = vec([0, -D/y, 0])
    elif axis == "z":
        p_0 = vec([0, 0, -D/z])
    return p_0

def plane_p_02D(n, p_0):
    """
    Convert p_0 from plane using normal vector to D for coordinate plane
    """
    D = -n.dot(p_0)
    return D

def plane_line_intersection(p_0, n, g, symbol_t):
    """
    Finds intersection point of a plane and a line
    """
    intersection_t = sp.solve(n.dot(p_0 - g), symbol_t)[0]
    T = g.subs({symbol_t:intersection_t})
    return T

def miror_point_on_plane(p_0, n, P):
    """
    Mirrors P relative to a plane
    """
    g, t = line(P, n)
    T = plane_line_intersection(p_0, n, g, t)
    PT = T - P
    P_mirrored = P + 2*PT
    return P_mirrored

def shortest_line2point(g, u, symbol_t, P):
    """
    finds the point on g that is closest to P
    u is the direcion vector of the line
    """
    gP = P - g
    closest_t = sp.solve(u.dot(gP), symbol_t)[0]
    P_closest = g.subs({symbol_t: closest_t})
    return P_closest

def mirror_vec_with_vec(a, b):
    """
    mirrors a with the b vector and returns c
    """
    e_b = b/b.norm() # einheitsvektor b
    b_a = e_b * a.dot(b)/b.norm() # anteil von a in richtung b
    c = 2*b_a - a # a spiegeln um b
    return c

def line_intersection(g1, g2):
    """
    finds the point where two lines intersect
    """
    intersect = g1 - g2
    intersect_solved = sp.solve(intersect)
    P = g1.subs(intersect_solved)
    return P
