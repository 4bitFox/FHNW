#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 13:45:34 2025

@author: cvetkofabian
"""

import sympy as sp
import matplotlib.pyplot as plt

def line(p1, p2 = sp.zeros(2, 1)):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], "k-", lw=2)
    plt.grid(True)
    
def lines_between_hstacked_points(M):
    plt.plot( [M[0,i] for i in range(M.shape[1])], [M[1,i] for i in range(M.shape[1])], "k-", lw=2)
    plt.grid(True)
    
def plt_3D(x = None, y = None, z = None):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    
    # Set labels for axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    # if data given; plot
    if x != None:
        ax.plot(x, y, z)
    return fig, ax
