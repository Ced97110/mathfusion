import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 22, 52, r'$\mathbb{T}$', 'sujet', 60.0)
text(ax, 22, 33, '« grand T à double barre »', 'fixe', 's')
arrow(ax, (40, 50), (50, 50), 'varie', lw=1.1)
cx, cy, r = 68, 50, 15
arrow(ax, (cx - r - 3, cy), (cx + r + 4, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - r - 3), (cx, cy + r + 4), 'fixe', lw=0.6)
disc(ax, cx, cy, r, 'sujet', fill=False, lw=1.4)
for a, lab, dx, dy, ha in [(0, '1', 2.5, 2.5, 'left'), (60, r'$\omega$', 2.5, 2.5, 'left'), (200, r'$\mathrm{cis}\,\theta$', -2.5, -2.5, 'right')]:
    x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
    disc(ax, x, y, 1.3, 'sujet')
    text(ax, x + dx, y + dy, lab, 'sujet', 's', ha=ha)
text(ax, cx, 26, 'tous les complexes de module 1', 'sujet', 's')
text(ax, 44, 11, r'$z\in\mathbb{T}$ veut dire $|z|=1$', 'resultat', 'l')
save(fig, '39-106')
