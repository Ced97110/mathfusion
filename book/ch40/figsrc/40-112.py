import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(82)
cx, cy, u = 44, 60, 16
c = 1.0
th = np.linspace(-math.pi / 4, math.pi / 4, 200)
r = np.sqrt(2 * c * c * np.cos(2 * th))
xr, yr = cx + u * r * np.cos(th), cy + u * r * np.sin(th)
line(ax, list(zip(xr, yr)), 'sujet', lw=1.3)
line(ax, list(zip(2 * cx - xr, yr)), 'sujet', lw=1.3)
fx1, fx2, mx = cx - c * u, cx + c * u, cx + math.sqrt(2) * u
for x in (fx1, fx2):
    disc(ax, x, cy, 1.1, 'autre')
disc(ax, mx, cy, 1.1, 'varie')
text(ax, fx1, cy + 3.5, r'$F_1$', 'autre', 's')
text(ax, fx2, cy + 3.5, r'$F_2$', 'autre', 's')
text(ax, mx + 3.5, cy + 3.5, r'$M$', 'varie', 's')
d1, d2 = mx - fx1, mx - fx2
for (xa, xb, y, role) in ((fx1, mx, 47, 'varie'), (fx2, mx, 39, 'varie')):
    line(ax, [(xa, y), (xb, y)], role, lw=1.1)
    line(ax, [(xa, y - 1.2), (xa, y + 1.2)], role, lw=1.1)
    line(ax, [(xb, y - 1.2), (xb, y + 1.2)], role, lw=1.1)
for x, y in ((fx1, 47), (fx2, 39), (mx, 39)):
    line(ax, [(x, cy - 1.5), (x, y)], 'fixe', lw=0.5, dash=True)
text(ax, (fx1 + mx) / 2, 50.5, r'$MF_1\approx 2{,}414$', 'varie', 's')
text(ax, (fx2 + mx) / 2, 35.5, r'$MF_2\approx 0{,}414$', 'varie', 's')
text(ax, 44, 29,r'$MF_1\times MF_2\approx 1=c^2$', 'resultat', 'm')
text(ax, 44, 77, r'$MF_1\times MF_2=c^2$', 'sujet', 'l')
save(fig, '40-112')
