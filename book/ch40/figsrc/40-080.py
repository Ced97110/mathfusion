import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(64)
cx, cy, gap = 24, 34, 3.0
pc(ax, lambda t: gap*t/(2*np.pi), 0, 10*np.pi, cx, cy, 1, 'sujet', 1.3, n=2000)
disc(ax, cx, cy, 0.7, 'encre')
xa, xb = cx + 3*gap, cx + 4*gap
arrow(ax, (xa + 0.4, cy), (xb - 0.4, cy), 'varie', lw=1.0, both=True)
line(ax, [((xa + xb)/2, cy + 0.8), (31, 54)], 'varie', lw=0.5)
text(ax, 31, 58, '0,1 mm entre deux tours', 'varie', 's')
text(ax, 70, 54, '0,1 = a × 2π', 'sujet', 'm')
text(ax, 70, 47, 'a = 0,1 ÷ 6,28', 'sujet', 'm')
box(ax, 53, 33, 33, 9, 'resultat', label='a ≈ 0,016 mm/rad', size='s')
text(ax, 70, 25, '10 tours : 62,8 rad', 'encre', 's')
text(ax, 70, 19, '0,016 × 62,8 ≈ 1 mm', 'encre', 's')
text(ax, 70, 13, '= 10 × 0,1 mm', 'resultat', 's')
save(fig, '40-080')
