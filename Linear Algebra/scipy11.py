# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:03:15 2022

@author: Teezzy
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq

t = np.linspace(0, 10*np.pi, 100)
x = np.sin(2*np.pi*t) + np.sin(4*np.pi*t) + 0.1*np.random.randn(len(t))

N = len(x)
y = fft(x)[:N//2]

f = fftfreq(N, np.diff(t)[0])[:N//2]

plt.plot(f, np.abs(y))
#plt.plot(t, x)
plt.show()