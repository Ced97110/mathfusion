import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$\tan(x+\pi)=\tan x$', 'encre', 'l')
for y, a, b, t in ((38, '1', '4,1416', '1,5574'), (10, '0,5', '3,6416', '0,5463')):
    box(ax, 6, y + 8, 30, 10, 'sujet', label=f'x = {a}', size='s')
    box(ax, 52, y + 8, 30, 10, 'varie', label=f'x + π = {b}', size='s')
    arrow(ax, (36.8, y + 13), (51.2, y + 13), 'varie'); text(ax, 44, y + 17, '+ π', 'varie', 's')
    box(ax, 6, y - 4, 30, 9, 'resultat', label=f'tan = {t}', size='s')
    box(ax, 52, y - 4, 30, 9, 'resultat', label=f'tan = {t}', size='s')
    text(ax, 44, y + 0.5, '=', 'resultat', 'l')
save(fig, '30-055')
