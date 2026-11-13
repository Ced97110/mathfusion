import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(62)
cy = 32
cx, u = 24, 20
th = np.linspace(-np.pi/4, np.pi/4, 500)
line(ax, [(cx - 22, cy), (cx + 22, cy)], 'fixe', lw=0.4)
for sgn in (1, -1):
    ax.plot(cx + u*sgn*np.sqrt(np.cos(2*th))*np.cos(th), cy + u*sgn*np.sqrt(np.cos(2*th))*np.sin(th), color=COL['sujet'], lw=1.5, zorder=3)
q = np.sqrt(0.5)
for sgn, name in ((-1, 'F₁'), (1, 'F₂')):
    disc(ax, cx + sgn*q*u, cy, 1.1, 'autre')
    text(ax, cx + sgn*q*u, cy - 4.5, name, 'autre', 's')
disc(ax, cx, cy, 0.7, 'encre')
text(ax, cx + 2.5, cy + 3, 'O', 'encre', 's')
text(ax, cx, 56, 'r² = cos 2θ  (a = 1)', 'sujet', 'm')
text(ax, cx, 8, 'deux boucles, deux foyers', 'sujet', 's')
sx, su = 66, 9
line(ax, [(sx, cy), (sx + 21, cy)], 'fixe', lw=0.4)
pc(ax, lambda t: t/(2*np.pi), 0, 4*np.pi, sx, cy, su, 'varie', 1.4)
for k in (1, 2):
    disc(ax, sx + k*su, cy, 0.9, 'encre')
    text(ax, sx + k*su, cy - 4.5, str(k), 'encre', 's')
disc(ax, sx, cy, 0.7, 'encre')
text(ax, sx, 56, 'r = θ/(2π)', 'varie', 'm')
text(ax, sx, 8, 'écart 1 à chaque tour', 'varie', 's')
save(fig, '40-076')
