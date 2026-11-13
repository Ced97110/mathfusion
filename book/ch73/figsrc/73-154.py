import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
text(ax, 44, 46, r'$(x,\ y)\mapsto(2x,\ y)$', 'varie', 'l')
box(ax, 5, 16, 20, 16, 'sujet', label='800 px', size='s')
box(ax, 45, 16, 40, 16, 'varie')
box(ax, 45, 16, 20, 16, 'sujet')
text(ax, 55, 24, '800 px', 'sujet', 's'); text(ax, 75, 24, '800 px', 'varie', 's')
text(ax, 15, 12, '1 000 px', 'sujet', 's'); text(ax, 65, 12, '2 000 px', 'varie', 's')
arrow(ax, (27, 24), (43, 24), 'varie'); text(ax, 35, 28, 'largeur × 2', 'varie', 's')
text(ax, 15, 37, 'aire 800 000', 'sujet', 's'); text(ax, 65, 37, 'aire 1 600 000', 'varie', 's')
text(ax, 44, 4, r'déterminant 2 $\neq$ 1', 'limite', 'm')
save(fig, '73-154')
