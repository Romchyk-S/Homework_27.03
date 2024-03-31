# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

def func_0():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = [-0.5]
    
    y_asymptote = [0.5]
    
    obl_asymptote = None
    
    label = f"$x = {x_asymptote} \ \ y = {y_asymptote} \ \ y = {obl_asymptote}$"
    
    title = "$y = (x-2)/(2x+1)$"
    
    return x, (x-2)/(2*x+1), label, title, x_asymptote, y_asymptote, obl_asymptote

def func_1():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = [1]
    
    y_asymptote = [None]
    
    obl_asymptote = (0, 2*0+2, 2)
    
    label = f"$x = {x_asymptote} \ \ y = {y_asymptote} \ \ y = 2x+2$"
    
    title = "$y = (2x^2)/(x-1)$"
    
    return x, (2*x**2)/(x-1), label, title, x_asymptote, y_asymptote, obl_asymptote

def func_2():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = [1, -1]
    
    y_asymptote = [1]
    
    obl_asymptote = None
    
    label = f"$x = {x_asymptote} \ \ y = {y_asymptote} \ \ y = {obl_asymptote}$"
    
    title = "$y = (x^2-4)/(x^2-1)$"
    
    return x, (x**2-4)/(x**2-1), label, title, x_asymptote, y_asymptote, obl_asymptote

def func_3():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = [-0.5]
    
    y_asymptote = [None]
    
    obl_asymptote = (0, 0/2-1/4, 1/2)
    
    label = f"$x = {x_asymptote} \ \ y = {y_asymptote} \ \ y = x/2-1/4$"
    
    title = "$y = (x^2)/(2x+1)$"
    
    return x, (x**2)/(2*x+1), label, title, x_asymptote, y_asymptote, obl_asymptote

def func_4():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = [-1, 1]
    
    y_asymptote = [None]
    
    obl_asymptote = (0, -1, -1)
    
    label = f"$x = {x_asymptote} \ \ y = {y_asymptote} \ \ y = -x$"
    
    title = "$y = (x^3)/(1-x^2)$"
    
    return x, (x**3)/(1-x**2), label, title, x_asymptote, y_asymptote, obl_asymptote

def func_5():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = [-1, 1]
    
    y_asymptote = [None]
    
    obl_asymptote = None
    
    label = f"$x = {x_asymptote} \ \ y = {y_asymptote} \ \ y = {obl_asymptote}$"
    
    title = "$y = (x^2)/(|x|-1)$"
    
    return x, (x**2)/(np.abs(x)-1), label, title, x_asymptote, y_asymptote, obl_asymptote
