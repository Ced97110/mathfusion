import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [(40, 2, 'plan : 2 coordonnées', 'produit connu : complexes', 'resultat'),
        (22, 3, 'espace : 3 coordonnées', 'pas de produit trouvé', 'limite'),
        (4, 4, 'en 1843 : 4 coordonnées', 'produit trouvé', 'resultat')]
for y, n, lab, st, ro in rows:
    text(ax, 4, y + 12, lab, 'sujet', 's', ha='left')
    for i in range(n):
        box(ax, 4 + 8 * i, y, 8, 8, 'sujet')
    text(ax, 42, y + 4, st, ro, 's', ha='left')
save(fig, '51-168')
