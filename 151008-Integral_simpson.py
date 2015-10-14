# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 07:53:51 2015

@author: antefe
"""
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.sin(t)

h = 0.1
x = np.arange(0,10.1,h)
simpson = np.empty(len(x))
int_sim =np.empty(len(x))

int_sim[0] = 0.0
for i in range(len(x)-2):
    simpson[i] = (h/3)*(f(x[i])+4*f(x[i+1])+f(x[i+2]))
    int_sim[i+1] = simpson[i]+int_sim[i]
    
print int_sim

plt.plot(x,int_sim,"go")
plt.show()