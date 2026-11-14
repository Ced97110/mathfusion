import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 4.8
cy = 32.0
items = [(15.0, r'$x^2+y^2=4$', 'plusieurs points', 'sujet'),
         (44.0, r'$x^2+y^2=0$', 'un seul point', 'resultat'),
         (73.0, r'$x^2+y^2=-1$', 'aucun point', 'limite')]
for cx, eq, cap, role in items:
    box(ax, cx - 13.5, 6, 27, 48, role, fill=False, lw=0.6, dash=True)
    arrow(ax, (cx - 11.5, cy), (cx + 11.5, cy), 'fixe', lw=0.5)
    arrow(ax, (cx, cy - 12), (cx, cy + 12), 'fixe', lw=0.5)
    text(ax, cx, 48.5, eq, role, 's')
    text(ax, cx, 10, cap, role, 's')
disc(ax, 15, cy, 2 * s, 'sujet', fill=False, lw=1.3)
disc(ax, 44, cy, 1.2, 'resultat')
save(fig, '70-007')
