import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, u = 22, 29, 3.6
arrow(ax, (cx - 21, cy), (cx + 21, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 21), (cx, cy + 21), 'fixe', lw=0.7)
disc(ax, cx, cy, 5 * u, 'sujet', fill=False, lw=1.4)
for (a, b) in [(3, 4), (4, 3), (5, 0), (0, 5), (-4, 3), (-3, -4), (0, -5), (-5, 0)]:
    disc(ax, cx + a * u, cy + b * u, 1.1, 'varie')
text(ax, cx + 3 * u + 1.5, cy + 4 * u + 3.2, r'(3 ; 4)', 'varie', 's', ha='left')
text(ax, cx, 3.5, 'cercle de rayon 5', 'sujet', 's')
arrow(ax, (cx + 5 * u + 3, cy), (51, cy), 'resultat')
box(ax, 52, cy - 6, 32, 12, 'resultat', label=r'$t$ = 25', size='l')
text(ax, 68, cy + 11, 'un seul nombre', 'resultat', 's')
text(ax, 68, cy - 11, 'somme des carrés', 'fixe', 's')
save(fig, '43-129')
