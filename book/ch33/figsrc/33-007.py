import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(52, '5', '15', '×3', '÷3', False), (32, '4', '16', 'carré', 'racine', False), (12, 'angle', '1/12', 'tan', '?', True)]
for y, a, b, fw, bw, ask in rows:
    box(ax, 4, y, 20, 10, 'sujet', label=a)
    box(ax, 64, y, 20, 10, 'autre', label=b)
    arrow(ax, (25, y + 7), (63, y + 7), 'fixe')
    arrow(ax, (63, y + 3), (25, y + 3), 'varie')
    text(ax, 44, y + 9.6, fw, 'fixe', 's')
    text(ax, 44, y + 0.2, bw, 'varie', 's')
save(fig, '33-007')
