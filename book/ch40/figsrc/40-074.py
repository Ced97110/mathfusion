import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(64)
cx, cy, u = 30, 32, 24
th = np.linspace(-np.pi/4, np.pi/4, 500)
for sgn in (1, -1):
    ax.plot(cx + u*sgn*np.sqrt(np.cos(2*th))*np.cos(th), cy + u*sgn*np.sqrt(np.cos(2*th))*np.sin(th), color=COL['fixe'], lw=1.0, zorder=2)
line(ax, [pp(cx, cy, 1, -27, 30*d2r), pp(cx, cy, 1, 27, 30*d2r)], 'fixe', lw=0.5, dash=True)
q = np.sqrt(0.5)
p1 = pp(cx, cy, u, q, 30*d2r); p2 = pp(cx, cy, u, -q, 30*d2r)
disc(ax, p1[0], p1[1], 1.1, 'sujet'); disc(ax, p2[0], p2[1], 1.1, 'varie')
disc(ax, cx, cy, 0.7, 'encre')
t = np.linspace(0, 30*d2r, 30)
ax.plot(cx + 5*np.cos(t), cy + 5*np.sin(t), color=COL['encre'], lw=0.7, zorder=3)
text(ax, cx + 8, cy + 2, '30°', 'encre', 's')
text(ax, cx + 3.5, cy - 4, 'O', 'encre', 's')
text(ax, 72, 54, 'r² = 0,5', 'encre', 'm')
text(ax, 72, 46, 'r = 0,707', 'sujet', 'm')
text(ax, 72, 41, 'point à 30°', 'sujet', 's')
text(ax, 72, 31, 'r = −0,707', 'varie', 'm')
text(ax, 72, 26, 'point à 210°', 'varie', 's')
text(ax, 30, 6, 'r = ± √(cos 2θ)', 'encre', 'm')
save(fig, '40-074')
