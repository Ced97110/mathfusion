import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(64)
u, cy = 17, 33
# left : cosine, axis of the x
cx = 22
line(ax, [(cx, cy - 19), (cx, cy + 19)], 'fixe', lw=0.4)
line(ax, [(cx - 19, cy), (cx + 19, cy)], 'encre', lw=1.0)
pc(ax, lambda t: np.cos(3*t), 0, 2*np.pi, cx, cy, u, 'sujet', 1.3)
a = pp(cx, cy, u, 0.5, 20*d2r); b = pp(cx, cy, u, 0.5, -20*d2r)
line(ax, [a, b], 'fixe', dash=True)
disc(ax, a[0], a[1], 0.9, 'resultat'); disc(ax, b[0], b[1], 0.9, 'resultat')
text(ax, a[0] + 3.2, a[1] + 1.8, '20°', 'resultat', 's')
text(ax, b[0] + 3.8, b[1] - 1.8, '−20°', 'resultat', 's')
text(ax, cx, 59, 'r = cos 3θ', 'sujet', 'm')
text(ax, cx, 8, 'symétrique : axe des x', 'resultat', 's')
# right : sine, axis of the y
cx = 66
line(ax, [(cx - 19, cy), (cx + 19, cy)], 'fixe', lw=0.4)
line(ax, [(cx, cy - 19), (cx, cy + 19)], 'encre', lw=1.0)
pc(ax, lambda t: np.sin(3*t), 0, 2*np.pi, cx, cy, u, 'autre', 1.3)
p30 = pp(cx, cy, u, 1, 30*d2r); p150 = pp(cx, cy, u, 1, 150*d2r); g = pp(cx, cy, u, 1, -30*d2r)
line(ax, [p30, p150], 'fixe', dash=True)
line(ax, [p30, g], 'limite', dash=True)
disc(ax, p30[0], p30[1], 0.9, 'resultat'); disc(ax, p150[0], p150[1], 0.9, 'resultat')
disc(ax, g[0], g[1], 1.0, 'limite', fill=False)
text(ax, p30[0] + 2, p30[1] + 4, '30°', 'resultat', 's')
text(ax, p150[0] - 2, p150[1] + 4, '150°', 'resultat', 's')
text(ax, 87, 17, 'pas de pétale', 'limite', 's', ha='right')
text(ax, cx, 59, 'r = sin 3θ', 'autre', 'm')
text(ax, cx, 8, 'symétrique : axe des y', 'resultat', 's')
save(fig, '40-063')
