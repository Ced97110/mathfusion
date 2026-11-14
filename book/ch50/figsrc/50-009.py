import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'Quels $d$ réussissent partout ?', 'encre', 'm')
ds = [1, 2, 3, 4, 6, 12]
xs = [32 + 10 * i for i in range(6)]
for x, d in zip(xs, ds): text(ax, x, 52, str(d), 'encre', 'm', weight='bold')
text(ax, 3, 52, r'$d$ =', 'encre', 's', ha='left')
rows = [(42, 'horloge', 'sujet', set()), (31, r'$A_4$', 'autre', {6})]
for y, name, role, bad in rows:
    text(ax, 3, y, name, role, 's', ha='left')
    for x, d in zip(xs, ds): disc(ax, x, y, 3.5, 'limite' if d in bad else 'resultat')
box(ax, 1.5, 11.5, 85, 13, 'fixe', fill=False, dash=True)
text(ax, 3.5, 18, 'tous les groupes ?', 'fixe', 's', ha='left')
for x, d in zip(xs, ds):
    if d == 6: disc(ax, x, 18, 3.5, 'limite')
    else: disc(ax, x, 18, 3.5, 'fixe', fill=False)
text(ax, 44, 6, 'vert : oui, rouge : non, vide : à prouver', 'encre', 's')
save(fig, '50-009')
