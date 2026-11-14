import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$x^4+1$', 'encre', 'l')
text(ax, 2, 58.5, r'sur $\mathbb{Q}$', 'sujet', 's', ha='left')
box(ax, 26, 54, 56, 9, 'sujet', label='irréductible : 1 facteur de degré 4', size='s')
for y, nm in [(40, 'modulo 3'), (26, 'modulo 5')]:
    text(ax, 2, y + 4.5, nm, 'encre', 's', ha='left')
    box(ax, 26, y, 27, 9, 'varie', label='degré 2', size='s')
    box(ax, 55, y, 27, 9, 'varie', label='degré 2', size='s')
text(ax, 44, 15, 'types 2 + 2 : aucun cycle de longueur 4', 'encre', 's')
text(ax, 44, 7, r'et pourtant irréductible sur $\mathbb{Q}$', 'sujet', 's')
save(fig, '67-236')
