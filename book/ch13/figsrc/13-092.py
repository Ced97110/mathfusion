import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 56, 'phrase', 'fixe', 's'); text(ax, 72, 56, 'symbole', 'sujet', 's')
for y, a, b in ((42, 3, 5), (22, 10, 12)):
    text(ax, 22, y, f'j’ai {a}, je dois {b}', 'fixe', 'm')
    arrow(ax, (42, y), (58, y), 'varie')
    text(ax, 72, y, f'({a}, {b})', 'sujet', 'l')
text(ax, 44, 7, r'modèle : $(a,\ b)$', 'sujet', 'm')
save(fig, '13-092')
