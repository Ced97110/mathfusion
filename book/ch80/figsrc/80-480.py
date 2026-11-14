import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
text(ax, 44, 67, 'chapitre 1 : réciter', 'sujet', 'm', weight='bold')
for j, v in enumerate('123'): disc(ax, 30 + j * 14, 55, 4.2, 'sujet', label=v)
arrow(ax, (44, 46), (44, 38), 'varie')
text(ax, 44, 33, 'chapitre 80 : de 1 à 30', 'resultat', 'm', weight='bold')
f = numberline(ax, 6, 82, 20, 1, 30, step=1, labels=False, arrow_right=False, tick=1.0)
for v in (1, 7, 11, 13, 17, 19, 23, 29): disc(ax, f(v), 20, 1.4, 'resultat')
text(ax, f(1), 14, '1', 'fixe', 's'); text(ax, f(30), 14, '30', 'fixe', 's')
text(ax, 44, 6, '8 entiers sans facteur avec 30', 'resultat', 's')
save(fig, '80-480')
