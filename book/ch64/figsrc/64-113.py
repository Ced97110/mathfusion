import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'élément de $A_n$ : 4 échanges', 'sujet', 's')
for k in range(4):
    box(ax, 3 + k * 21, 48, 19, 9, 'varie', label='échange', size='s')
for a, b, lab in ((3, 40, 'paire 1'), (45, 82, 'paire 2')):
    brace(ax, a, b, 48, 'varie', label=lab, size='s')
arrow(ax, (21.5, 38), (21.5, 30), 'fixe'); arrow(ax, (63.5, 38), (63.5, 30), 'fixe')
box(ax, 3, 15, 38, 14, 'resultat', label=r'$(1\,2)(3\,4)=(1\,3\,2)(1\,3\,4)$', size='s')
box(ax, 47, 15, 38, 14, 'resultat', label='produit de 3-cycles', size='s')
text(ax, 44, 6, r'donc $A_n$ : produits de 3-cycles', 'resultat', 's')
save(fig, '64-113')
