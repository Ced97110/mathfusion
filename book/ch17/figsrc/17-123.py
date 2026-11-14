import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
f = numberline(ax, 22, 62, 12, 0, 5, labels=False, arrow_right=True)
for v in (2, 3):
    text(ax, f(v), 7, f'{v}', 'encre', 's')
    line(ax, [(f(v), 12), (f(v), 68)], 'fixe', dash=True)
rows = [(60, 2, 'sujet', r'$x-2$', '−++'), (44, 3, 'autre', r'$x-3$', '−−+')]
zones = [(f(0) + 1, f(2)), (f(2), f(3)), (f(3), 80)]
for y, a, role, lab, signs in rows:
    text(ax, 2, y + 2, lab, role, 's', ha='left')
    line(ax, [(f(a), y + 5), (80, y + 5)], role, lw=2.8)
    disc(ax, f(a), y + 5, 1.2, role, fill=False)
    for (z0, z1), s in zip(zones, signs):
        text(ax, (z0 + z1) / 2, y - 1, s, role, 'l', weight='bold')
text(ax, 2, 26, 'produit', 'resultat', 's', ha='left')
for (z0, z1), s in zip(zones, '+−+'):
    text(ax, (z0 + z1) / 2, 26, s, 'resultat', 'l', weight='bold')
save(fig, '17-123')
