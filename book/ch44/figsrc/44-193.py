import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, a, b, note, nrole):
    box(ax, 4, y, 22, 10, 'fixe', label=a)
    arrow(ax, (26.5, y + 5), (33.5, y + 5), 'fixe')
    box(ax, 34, y, 20, 10, 'sujet', label=r'$I$', size='l')
    arrow(ax, (54.5, y + 5), (61.5, y + 5), 'fixe')
    box(ax, 62, y, 22, 10, nrole, label=b)
    text(ax, 44, y - 4.5, note, nrole, 's')
row(50, r'$(x,\ y)$', r'$(x,\ y)$', 'aucun point ne bouge', 'resultat')
row(27, r'$A$', r'$A$', r'$A$ reste telle quelle', 'resultat')
text(ax, 44, 17.5, 'et pour une matrice et son inverse :', 'fixe', 's')
box(ax, 14, 3, 60, 10, 'resultat', label=r'$A \times A^{-1} = I$')
save(fig, '44-193')
