import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 58, '$3\\times k$ sur 7 : le 1 sort', 'sujet', 's')
text(ax, 66, 58, '$2\\times k$ sur 6 : jamais 1', 'limite', 's')
for i, v in enumerate((3, 6, 2, 5, 1, 4)):
    box(ax, 2 + i * 6.8, 34, 6, 10, 'resultat' if v == 1 else 'fixe', label=str(v), size='s', r=0.5)
for i, v in enumerate((2, 4, 0, 2, 4)):
    box(ax, 46 + i * 8, 34, 7, 10, 'fixe', label=str(v), size='s', r=0.5)
arrow(ax, (22, 33), (22, 22), 'resultat')
box(ax, 2, 6, 40, 14, 'resultat', label='inverse de 3 : 5', size='s')
arrow(ax, (66, 33), (66, 22), 'limite')
box(ax, 46, 6, 40, 14, 'limite', label='2 sans inverse', size='s')
save(fig, '51-281')
