import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
s = 10   # décalage du bloc des modules
b = 3
rows = [(76 + s, '95 = 5 × 19'), (64 + s, '97, nombre premier'), (52 + s, '98 = 2 × 7 × 7'), (40 + s, '99 = 3 × 3 × 11')]
for y, t in rows:
    box(ax, 2, y - 4.5, 58, 9, 'sujet')
    text(ax, 5, y, t, 'sujet', 'm', ha='left')
line(ax, [(62, 80.5 + s), (64, 80.5 + s), (64, 35.5 + s), (62, 35.5 + s)], 'fixe')
text(ax, 75, 58 + s, 'tous < 100', 'fixe', 's')
text(ax, 2, 38, 'premiers entre eux deux à deux', 'varie', 's', ha='left')
text(ax, 2, 27 + b, 'produit des modules', 'sujet', 's', ha='left')
box(ax, 2, 16 + b, 84, 7, 'sujet', label='89 403 930')
box(ax, 2, 5 + b, 3.1, 7, 'resultat')
text(ax, 8, 8.5 + b, '3 267 154 : le résultat', 'resultat', 's', ha='left')
text(ax, 44, 2.5, '89 403 930 > 3 267 154', 'resultat', 'm')
save(fig, '52-252')
