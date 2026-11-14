import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
c3, r3 = 3 ** (1 / 3), math.sqrt(3)
assert abs(c3 * r3 - 3 ** (5 / 6)) < 1e-12 and abs(1 / 3 + 1 / 2 - 5 / 6) < 1e-12
cx, cy, u = 32, 24, 14.0
px, py = cx - c3 / 2 * u, cy + c3 * r3 / 2 * u      # j x racine cubique de 3
arrow(ax, (4, cy), (47, cy), 'fixe', lw=0.9)
arrow(ax, (cx, 6), (cx, 66), 'fixe', lw=0.9)
line(ax, [(cx, cy), (px, cy)], 'varie', lw=1.8)
line(ax, [(px, cy), (px, py)], 'sujet', lw=1.8)
line(ax, [(cx, cy), (px, py)], 'fixe', lw=0.8, dash=True)
disc(ax, px, py, 2.0, 'sujet')
text(ax, px, py + 5, r'$j\sqrt[3]{3}$', 'sujet', 'm')
text(ax, (cx + px) / 2, cy - 5, r'$-\dfrac{\sqrt[3]{3}}{2}$', 'varie', 's')
text(ax, px - 2.5, (cy + py) / 2, r'$\dfrac{\sqrt[3]{3}\,\sqrt{3}}{2}$', 'sujet', 's', ha='right')
# écrire le produit en une seule racine
box(ax, 52, 54, 34, 10, 'fixe', label=r'$\sqrt[3]{3}=3^{1/3}$', size='s')
text(ax, 69, 49.5, '+', 'encre', 'l')
box(ax, 52, 36, 34, 10, 'fixe', label=r'$\sqrt{3}=3^{1/2}$', size='s')
arrow(ax, (69, 36), (69, 29), 'varie', lw=1.0)
box(ax, 52, 19, 34, 10, 'varie', label=r'$\frac{1}{3}+\frac{1}{2}=\frac{5}{6}$', size='s')
arrow(ax, (69, 19), (69, 12), 'resultat', lw=1.0)
box(ax, 48, 1, 38, 11, 'resultat', label=r'$\sqrt[3]{3}\times\sqrt{3}=(\sqrt[6]{3})^5$', size='s')
save(fig, '62-151')
