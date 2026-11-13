import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
text(ax, 44, 51, 'un fil porte 0 ou 1', 'encre', 'm', weight='bold')
line(ax, [(10, 36), (34, 36)], 'fixe'); line(ax, [(10, 18), (34, 18)], 'fixe')
disc(ax, 8, 36, 4.2, 'fixe', label='0'); disc(ax, 8, 18, 4.2, 'sujet', label='1')
line(ax, [(34, 36), (42, 30)], 'fixe'); line(ax, [(34, 18), (42, 24)], 'fixe')
box(ax, 40, 21, 16, 12, 'varie', label='ou')
line(ax, [(56, 27), (68, 27)], 'fixe')
disc(ax, 74, 27, 4.2, 'resultat', label='1')
text(ax, 44, 6, 'un des deux porte 1 : sortie 1', 'resultat', 's')
save(fig, '80-477')
