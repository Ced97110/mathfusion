import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, s = 14, 10, 6.5
for a in range(7):
    for b in range(7):
        disc(ax, ox + a * s, oy + b * s, 0.5, 'fixe')
line(ax, [(ox, oy), (ox + 6 * s, oy + 6 * s)], 'fixe', dash=True)
text(ax, ox + 6.4 * s, oy + 6.6 * s, 'droite de 0', 'fixe', 's', ha='left')
for (a, b), r in [((3, 5), 'sujet'), ((5, 2), 'autre')]:
    disc(ax, ox + a * s, oy + b * s, 1.5, r)
    arrow(ax, (ox + a * s - 1, oy + b * s - 1.4), (ox + 1.5, oy + 1.5), 'varie')
text(ax, ox + 3 * s - 2, oy + 5 * s + 3, '(3, 5)', 'sujet', 's')
text(ax, ox + 5 * s + 2, oy + 2 * s + 3, r'$(a,b)$', 'autre', 's', ha='left')
disc(ax, ox, oy, 1.7, 'resultat')
text(ax, ox + 2, oy - 4, '(0, 0)', 'resultat', 's')
box(ax, 52, 20, 33, 9, 'varie', label=r'$\times (0,0)$')
text(ax, 68, 14, 'même résultat', 'resultat', 's')
save(fig, '13-136')
