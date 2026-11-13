import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(98)
text(ax, 29, 92, 'reste par 55', 'fixe', 's')
text(ax, 63, 92, 'bit', 'fixe', 's')
rows = [(17, 1), (14, 1), (31, 0), (26, 1), (16, 1)]
for i, (v, bit) in enumerate(rows):
    y = 76 - 16 * i
    role = 'resultat' if bit else 'fixe'
    box(ax, 12, y, 34, 10, role, label=str(v))
    box(ax, 56, y, 14, 10, role, label=str(bit))
    line(ax, [(46.5, y + 5), (55.5, y + 5)], role, lw=1.2)
    if not bit:
        text(ax, 78, y + 5, 'non utilisée', 'fixe', 's')
    if i < 4:
        arrow(ax, (29, y - 0.5), (29, y - 5.5), 'varie')
text(ax, 44, 3.5, '27 = 16 + 8 + 2 + 1 = 11011', 'sujet', 's')
save(fig, '53-132')
