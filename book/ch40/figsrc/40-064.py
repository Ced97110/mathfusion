import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(56)
u, cy = 6.5, 32
panels = [(5, lambda t: 2*np.cos(t), 'autre', 'cercle', 'r = 2 cos θ', 'a = 0, b = 2'),
          (38, lambda t: 2 + np.cos(t), 'sujet', 'limaçon', 'r = 2 + cos θ', 'a = 2, b = 1'),
          (68, lambda t: 1 + np.cos(t), 'autre', 'cardioïde', 'r = 1 + cos θ', 'a = 1, b = 1')]
for ox, f, role, name, eq, ab in panels:
    pc(ax, f, 0, 2*np.pi, ox, cy, u, role, 1.4)
    disc(ax, ox, cy, 0.7, 'encre')
    mid = ox + (6.5 if name == 'cercle' else (13 if name == 'limaçon' else 6.5))
    text(ax, mid, 52, name, role, 'm')
    text(ax, mid, 12, eq, role, 's')
    text(ax, mid, 6, ab, 'encre', 's')
save(fig, '40-064')
