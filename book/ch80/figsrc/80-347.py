import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
box(ax, 10, 52, 68, 9, 'resultat', label=r'il faut PPCM$(2,x)=12$')
text(ax, 44, 44, r'candidats : PGCD$(2,x)=1$', 'fixe', 's')
for i, (x, v) in enumerate([(1, 2), (3, 6)]):
    y = 26 - 16 * i
    box(ax, 4, y, 14, 9, 'sujet', label=f'x = {x}')
    arrow(ax, (19, y + 4.5), (31, y + 4.5), 'varie')
    box(ax, 32, y, 36, 9, 'limite', label=f'PPCM(2, {x}) = {v}')
    text(ax, 78, y + 4.5, '≠ 12', 'limite', 'm')
save(fig, '80-347')
