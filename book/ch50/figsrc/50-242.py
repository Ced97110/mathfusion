import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 3, 24, 24, 14, 'sujet', label=r'$|G| = 15$', size='l')
arrow(ax, (29, 31), (43, 31), 'varie'); text(ax, 36, 35, 'Sylow', 'varie', 's')
cx, cy, R = 66, 33, 15
P = [(cx + R * math.cos(math.radians(90 - 24 * k)), cy + R * math.sin(math.radians(90 - 24 * k))) for k in range(15)]
line(ax, [P[k] for k in (0, 5, 10, 0)], 'sujet', lw=1.1)
line(ax, [P[k] for k in (0, 3, 6, 9, 12, 0)], 'autre', lw=1.1)
for k, p in enumerate(P):
    r = 'encre' if k == 0 else ('sujet' if k % 5 == 0 else ('autre' if k % 3 == 0 else 'fixe'))
    disc(ax, p[0], p[1], 1.7, r)
text(ax, 66, 54, 'cyclique', 'resultat', 'm', weight='bold')
disc(ax, 45, 10, 1.7, 'sujet'); text(ax, 49, 10, 'un seul de 3 éléments', 'sujet', 's', ha='left')
disc(ax, 45, 4, 1.7, 'autre'); text(ax, 49, 4, 'un seul de 5 éléments', 'autre', 's', ha='left')
save(fig, '50-242')
