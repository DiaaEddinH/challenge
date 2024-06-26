#!/usr/bin/env python

import numpy as np
from matplotlib.pyplot import colorbar, show, subplots, savefig

results = np.loadtxt("results/data.dat")

fig, ax = subplots()
image = ax.imshow(results, vmin=-3, vmax=3, extent=(-1, 1, -1, 1))
cbar = colorbar(image, ax=ax,
                ticks=(-4*np.pi/5, -2*np.pi/3, 0, 2*np.pi/5, 4*np.pi/5))
cbar.set_label(r'$\arg(z_n)$')
cbar.ax.set_yticklabels((r'$-\frac{4\pi}{5}$', r'$-\frac{2\pi}{5}$', '0',
                         r'$\frac{2\pi}{5}$', r'$\frac{4\pi}{5}$'))
ax.set_xlabel(r'$\operatorname{Re}(z_0)$')
ax.set_ylabel(r'$\operatorname{Im}(z_0)$')

savefig('results/fig2.png')
