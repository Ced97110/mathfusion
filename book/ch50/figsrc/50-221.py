import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for x, role, l in [(4, 'sujet', r'$n_p=1$'), (33, 'sujet', 'Sylow unique,\nnormal'), (62, 'resultat', 'groupe non\nsimple')]:
    box(ax, x, 58, 22, 11, role, label=l, size='s')
arrow(ax, (26.5, 63.5), (32.5, 63.5), 'fixe')
arrow(ax, (55.5, 63.5), (61.5, 63.5), 'fixe')
text(ax, 44, 50, '60 = 5 × 12 : diviseurs de 12', 'encre', 's')
divs = [1, 2, 3, 4, 6, 12]
for i, d in enumerate(divs):
    r = d % 5
    box(ax, 2.5 + 14.1 * i, 30, 12.5, 14, 'varie' if r == 1 else 'limite', label=f'{d}\nreste {r}', size='s')
text(ax, 65, 25, r'cas de $A_5$ (simple)', 'autre', 's')
box(ax, 4, 4, 80, 13, 'limite', label='deux valeurs : 1 ou 6\nla méthode ne conclut pas', size='s')
save(fig, '50-221')
