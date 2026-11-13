import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 9.0; x0 = 14.0
X = lambda v: x0 + (v - 1) * (s + 2.5) + s / 2
rows = [(4, [1, 2, 4], 'sujet', 44), (6, [1, 2, 3, 6], 'autre', 28)]
for nb, divs, role, y in rows:
    text(ax, 5, y + 4.5, f'{nb}', role, 'm')
    for d in divs:
        box(ax, X(d) - s / 2, y, s, s, role, label=str(d), r=0.6, weight='bold' if d == 2 else 'normal')
for d in (1, 2):
    line(ax, [(X(d), 44), (X(d), 37)], 'resultat', lw=1.1)
ax.add_patch(Rectangle((X(1) - s / 2 - 1, 26.5), 2 * (s + 2.5) - 1.5 + 2 - 1, 29 , ec=COL['resultat'], fc='none', lw=1.0, ls='--', zorder=1))
text(ax, X(1.5)+8, 60, 'communs : 1 et 2', 'resultat', 's')
box(ax, 24, 3, 40, 10, 'resultat', label='PGCD(4, 6) = 2', size='l', weight='bold')
text(ax, 70, 8, 'le plus grand', 'resultat', 's', ha='left') if False else None
arrow(ax, (X(2), 26), (X(2), 14), 'resultat')
save(fig, '45-195')
