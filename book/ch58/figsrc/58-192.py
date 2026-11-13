import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# deux preuves, deux domaines : le déterminant couvre les anneaux commutatifs, l'échange couvre les corps
box(ax, 3, 4, 82, 66, 'fixe', r=2)
text(ax, 44, 66, 'preuve par le déterminant :', 'fixe', 's', weight='bold')
text(ax, 44, 61.5, 'tout anneau commutatif', 'fixe', 's', weight='bold')
box(ax, 8, 8, 72, 33, 'autre', r=2)
text(ax, 44, 36, 'preuve par échange :', 'autre', 's', weight='bold')
text(ax, 44, 31.5, 'seulement un corps', 'autre', 's', weight='bold')
box(ax, 22, 11, 44, 15, 'sujet', label='plan réel : dimension 2', size='s', r=1)
box(ax, 8, 46, 72, 10, 'sujet', label='couples d’entiers : rang 2', size='s', r=1)
save(fig, '58-192')
