import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(62)
cx, cy, u = 30, 31, 24
for k in range(6):
    a = k*30*d2r
    line(ax, [pp(cx, cy, 1, -25.5, a), pp(cx, cy, 1, 25.5, a)], 'fixe', lw=0.35)
pc(ax, lambda t: np.cos(3*t), 0, 2*np.pi, cx, cy, u, 'fixe', 0.9)
vals = [(0, 1), (30, 0), (60, -1), (90, 0), (120, 1), (150, 0), (180, -1)]
for deg, r in vals:
    if r == 0: continue
    role = 'sujet' if r > 0 else 'varie'
    x, y = pp(cx, cy, u, r, deg*d2r)
    disc(ax, x, y, 1.1, role, fill=(deg != 180))
disc(ax, cx, cy, 0.6, 'encre')
text(ax, 57, cy + 8, '0° et 180°', 'encre', 's', ha='right')
x, y = pp(cx, cy, u, -1, 60*d2r)
text(ax, x - 8, y - 4, '60° : recule', 'varie', 's')
x, y = pp(cx, cy, u, 1, 120*d2r)
text(ax, x - 3, y + 4, '120°', 'sujet', 's')
text(ax, cx, 59, 'r = cos 3θ', 'sujet', 'm')
text(ax, 73, 54, 'tous les 30°', 'encre', 's')
for i, (deg, r) in enumerate(vals):
    rs = f'{r}'.replace('-', '−')
    role = 'sujet' if r > 0 else ('varie' if r < 0 else 'fixe')
    text(ax, 62, 48 - i*6.2, f'θ = {deg}° : r = {rs}', role, 's', ha='left')
save(fig, '40-058')
