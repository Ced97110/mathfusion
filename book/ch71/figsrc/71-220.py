import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
# left: one sheet around vertical axis z (rings stacked)
c = (22, 40); u = 8
zs = np.linspace(-1.6, 1.6, 9)
for z in zs:
    r = (1 + z*z) ** 0.5
    t = np.linspace(0, 2*np.pi, 80)
    ax.plot(c[0] + r*u*np.cos(t), c[1] + z*u + 0.3*r*u*np.sin(t), color=COL['sujet'], lw=0.7, zorder=2)
for sg in (-1, 1):
    zz = np.linspace(-1.6, 1.6, 60)
    ax.plot(c[0] + sg*u*np.sqrt(1+zz**2), c[1] + zz*u, color=COL['sujet'], lw=1.3, zorder=3)
arrow(ax, (c[0], c[1]-15), (c[0], c[1]+17), 'fixe', lw=0.6); text(ax, c[0]+3, c[1]+17, r'$z$', 'fixe', 's')
text(ax, 22, 14, r'$x^2+y^2-z^2=1$', 'sujet', 's'); text(ax, 22, 8, '(2, 1) : un morceau', 'sujet', 's')
# right: two sheets along x axis
d = (66, 40); v = 8
arrow(ax, (d[0]-21, d[1]), (d[0]+21, d[1]), 'fixe', lw=0.6); text(ax, d[0]+21, d[1]-3, r'$x$', 'fixe', 's')
for sg in (-1, 1):
    for x in (1, 1.25, 1.5, 1.75, 2):
        r = (x*x - 1) ** 0.5
        t = np.linspace(0, 2*np.pi, 80)
        ax.plot(d[0] + sg*x*v + 0.3*r*v*np.cos(t), d[1] + r*v*np.sin(t), color=COL['autre'], lw=0.7, zorder=2)
    xx = np.linspace(1, 2, 40)
    for s2 in (-1, 1):
        ax.plot(d[0] + sg*xx*v, d[1] + s2*v*np.sqrt(xx**2-1), color=COL['autre'], lw=1.3, zorder=3)
text(ax, d[0], d[1]+13, r'$|x|<1$ : vide', 'limite', 's')
text(ax, 66, 14, r'$x^2-y^2-z^2=1$', 'autre', 's'); text(ax, 66, 8, '(1, 2) : deux morceaux', 'autre', 's')
text(ax, 44, 64, r'$p$ et $q$ changent : lequel décide ?', 'encre', 's')
save(fig, '71-220')
