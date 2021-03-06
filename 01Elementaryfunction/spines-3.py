#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
X = np.linespace(-np.pi, +np.pi, 256)
Y = np.sin(X)

# Actual plotting
fig = plt.figure(figsize=(8, 6), dpi=72, facecolor='white')
axes = plot.subplot(111)
axes.plot(X, Y, color='blue', linewidth=2, linestyle='-')
axes.set_xlim(X.min(), X.max())
axes.set_ylim(Y.min(), y.max())
