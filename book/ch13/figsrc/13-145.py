import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
box(ax, 3, 14, 52, 36, 'sujet', dash=True)
text(ax, 29, 54, 'une classe : −2', 'sujet', 's')
for i, p in enumerate(['(1, 3)', '(0, 2)', '(2, 4)']):
    box(ax, 8 + i * 15.5, 26, 14, 9, 'sujet', label=p, size='s')
text(ax, 29, 19, 'classe = un seul objet', 'sujet', 's')
box(ax, 61, 14, 24, 36, 'autre', dash=True)
text(ax, 73, 54, 'une autre : 2', 'autre', 's')
for i, p in enumerate(['(3, 1)', '(4, 2)']):
    box(ax, 66, 34 - i * 12, 14, 9, 'autre', label=p, size='s')
text(ax, 44, 6, 'aucun couple dans deux classes', 'resultat', 's')
save(fig, '13-145')
