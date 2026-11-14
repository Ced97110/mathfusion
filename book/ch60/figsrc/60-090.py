import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, 'partitions de 3', 'sujet', 'm')
rows = [(38, '3', [3]), (24, '2 + 1', [2, 1]), (10, '1 + 1 + 1', [1, 1, 1])]
for y, lab, parts in rows:
    text(ax, 4, y + 5, lab, 'sujet', 'm', ha='left')
    x = 30
    for v in parts:
        box(ax, x, y, 7 * v - 1.5, 10, 'sujet', r=0.5)
        x += 7 * v + 1.5
arrow(ax, (54, 29), (60, 29), 'resultat')
text(ax, 72, 29, 'P(3) = 3', 'resultat', 'l')
save(fig, '60-090')
