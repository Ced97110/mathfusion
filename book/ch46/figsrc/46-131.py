import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, x0, y, n, roles, labels=None, st=5.6, w=5.0, h=5.0):
    for k in range(1, n + 1):
        r = roles.get(k)
        box(ax, x0 + (k - 1) * st, y, w, h, r or "fixe", fill=r is not None, dash=r is None,
            label=(labels or {}).get(k), size="s", r=0.6)

fig, ax = canvas(62)
text(ax, 2, 57, "groupe cyclique d'ordre 6", 'sujet', 'm', ha='left')
row(ax, 6, 45, 6, {1: 'resultat', 5: 'resultat'}, {1: '1', 5: '5'}, st=11, w=10, h=7)
text(ax, 2, 40, '1 et 5 premiers avec 6 : 2 générateurs', 'resultat', 's', ha='left')
text(ax, 2, 28, 'permutations de 3 cartes : 6 éléments', 'autre', 'm', ha='left')
row(ax, 6, 16, 6, {k: 'limite' for k in range(1, 7)}, st=11, w=10, h=7)
text(ax, 2, 11, 'pas cyclique : aucun générateur', 'limite', 's', ha='left')
save(fig, '46-131')
