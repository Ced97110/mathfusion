import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
pitch = 17.5; bw = 14
def bx(i, y, lab, role):
    box(ax, 2 + i * pitch, y, bw, 9, role, label=lab, size='s')
text(ax, 44, 79, '2 échanges de voisins', 'varie', 's')
for i, (lab, r) in zip([0, 2, 4], [('3 1 2', 'sujet'), ('1 3 2', 'fixe'), ('1 2 3', 'resultat')]):
    bx(i, 62, lab, r)
for i in (0, 2): arrow(ax, (2 + i * pitch + bw + 0.5, 66.5), (2 + (i + 2) * pitch - 0.5, 66.5), 'varie')
text(ax, 44, 46, '4 échanges de voisins', 'varie', 's')
for i, (lab, r) in enumerate([('3 1 2', 'sujet'), ('3 2 1', 'fixe'), ('2 3 1', 'fixe'), ('2 1 3', 'fixe'), ('1 2 3', 'resultat')]):
    bx(i, 30, lab, r)
for i in range(4): arrow(ax, (2 + i * pitch + bw + 0.3, 34.5), (2 + (i + 1) * pitch - 0.3, 34.5), 'varie')
box(ax, 14, 6, 60, 12, 'resultat', label=r'pair dans les deux cas : signe $+1$')
save(fig, '76-056')
