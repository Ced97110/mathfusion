import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
assert 2 - 2 + 3 * 8 == 24
text(ax, 22, 51, r'$A$', 'sujet', 'l')
cw = 9
for i, v in enumerate([2, -1, 0, 3]):
    box(ax, 4 + i * cw, 34, cw - 0.8, 9, 'sujet', label=str(v).replace('-', '−'), size='s')
text(ax, 22, 28, 'polynôme : une suite', 'sujet', 's')
arrow(ax, (41, 38.5), (56, 38.5), 'varie')
text(ax, 48.5, 43.5, 'évaluation', 'varie', 's')
text(ax, 48.5, 33.5, r'$x\mapsto2$', 'varie', 's')
text(ax, 70, 51, r'$A(2)$', 'resultat', 'l')
box(ax, 58, 34, 24, 9, 'resultat', label='24', size='l')
text(ax, 70, 28, 'valeur : un nombre', 'resultat', 's')
text(ax, 44, 12, 'deux objets de nature différente', 'encre', 's')
save(fig, '54-110')
