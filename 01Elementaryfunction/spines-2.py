#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
X = np.linspace(-np.pi, +np.pi, 256)
Y = np.sin(X)

# Actual plotting
fig = plt.figure(figsize=(8, 6), dpi=72, facecolor="white")
axes = plt.subplot(111)
axes.plot(X, Y, color='blue', linewidth=2, linestyle="-")
axes.set_xlim(X.min(), X.max())
axes.set_ylim(1.00 * Y.min(), 1.00 * Y.max())

axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')

plt.show()
