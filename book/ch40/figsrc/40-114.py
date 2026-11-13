import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
cx, cy, u = 44, 44, 30
a = 1.0
c = a / math.sqrt(2)
th = np.linspace(-math.pi / 4, math.pi / 4, 200)
r = a * np.sqrt(np.cos(2 * th))
xr, yr = cx + u * r * np.cos(th), cy + u * r * np.sin(th)
line(ax, list(zip(xr, yr)), 'sujet', lw=1.3)
line(ax, list(zip(2 * cx - xr, yr)), 'sujet', lw=1.3)
line(ax, [(cx - 33, cy), (cx + 33, cy)], 'fixe', lw=0.6)
for s in (-1, 1):
    disc(ax, cx + s * c * u, cy, 1.1, 'autre')
    disc(ax, cx + s * a * u, cy, 1.1, 'sujet')
disc(ax, cx, cy, 0.8, 'fixe')
text(ax, cx - c * u, cy + 3.5, r'$F_1$', 'autre', 's')
text(ax, cx + c * u, cy + 3.5, r'$F_2$', 'autre', 's')
text(ax, cx + a * u + 4.5, cy + 3.5, r'$(1\,;\,0)$', 'sujet', 's')
for (x1, y, lab, role) in ((cx + c * u, 31, r'$c=1/\sqrt{2}\approx 0{,}707$', 'autre'), (cx + a * u, 20, r'$a=1$', 'sujet')):
    brace(ax, cx, x1, y, role, label=lab)
    line(ax, [(x1, cy - 1.5), (x1, y)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 7, r'$a^2=2c^2$ : $1=2\times 0{,}5$', 'resultat', 's')
text(ax, 44, 58, r'foyers en $\pm c$ sur l’axe', 'encre', 'm')
save(fig, '40-114')
