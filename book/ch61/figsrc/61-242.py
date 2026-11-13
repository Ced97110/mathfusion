import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, u = 40, 34, 12
box(ax, 3, cy - 3.5, 82, 7, 'sujet', fill=False, dash=True)
disc(ax, cx, cy, 20, 'resultat', fill=False, lw=1.0)
pts = [(cx + 1.26 * u, cy, 'sujet'), (cx - 0.63 * u, cy + 1.09 * u, 'limite'), (cx - 0.63 * u, cy - 1.09 * u, 'limite')]
for x, y, r in pts: disc(ax, x, y, 1.8, r)
text(ax, cx + 1.26 * u + 6.5, cy + 5.5, r'$\sqrt[3]{2}$', 'sujet', 's')
text(ax, cx - 0.63 * u + 9.5, cy + 1.09 * u + 3, 'non réelle', 'limite', 's')
text(ax, cx - 0.63 * u + 9.5, cy - 1.09 * u - 3, 'non réelle', 'limite', 's')
text(ax, 44, 61, 'corps de décomposition : toutes les racines', 'resultat', 's')
text(ax, 62, 25.5, r'corps de $\sqrt[3]{2}$ : réels', 'sujet', 's')
save(fig, '61-242')
