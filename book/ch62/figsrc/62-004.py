import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# top : cassé en trois facteurs
text(ax, 44, 74, 'se casse : 3 facteurs, 3 racines', 'encre', 'm')
for i, (fac, r) in enumerate([('$x-1$', '1'), ('$x-2$', '2'), ('$x-3$', '3')]):
    x = 8 + i * 27
    box(ax, x, 55, 22, 10, 'sujet', label=fac)
    arrow(ax, (x + 11, 54.5), (x + 11, 47.5), 'varie')
    disc(ax, x + 11, 44.5, 3, 'resultat', label=r)
line(ax, [(4, 36), (84, 36)], 'fixe', lw=0.6)
# bottom : x^3 - 2
text(ax, 44, 31, '$x^3-2$ : une seule racine réelle', 'encre', 'm')
box(ax, 8, 14, 22, 10, 'sujet', label='$x-$∛2')
box(ax, 35, 14, 22, 10, 'varie', fill=False, dash=True, label='?')
box(ax, 62, 14, 22, 10, 'varie', fill=False, dash=True, label='?')
brace(ax, 35, 84, 12, 'varie', label='2 racines manquantes')
save(fig, '62-004')
