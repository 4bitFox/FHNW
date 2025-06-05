#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 17:20:04 2025

@author: cvetkofabian
"""

import sympy as sp

def eigenvects_normed(A):
    """
    Returns eigenvals and eigenvectors of a matrix but normed.
    """
    A_eig = A.eigenvects()

    eigenvects = []
    for eiglist in A_eig:
        for eig in eiglist[2]:
            eig = eig / eig.norm()
            eigenvects.append([eiglist[0], eig])
    
    return eigenvects
