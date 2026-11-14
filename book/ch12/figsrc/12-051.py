import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for cx, role, head, rows in [(22, 'sujet', 'avec parenthèses', ['8 · (3 + 6)', '(3 + 6) = 9', '8 · 9 = 72']),
                              (66, 'autre', 'sans parenthèses', ['8 · 3 + 6', '8 · 3 = 24', '24 + 6 = 30'])]:
    text(ax, cx, 60, head, role, 'm')
    ys = [44, 28, 12]
    for i, (y, s) in enumerate(zip(ys, rows)):
        box(ax, cx - 19, y, 38, 11, role if i == 0 else 'fixe' if i == 1 else role, label=s, size='m')
        if i < 2: arrow(ax, (cx, y - 0.5), (cx, y - 4.5), 'varie')
text(ax, 44, 17.5, '≠', 'encre', 'xl')
save(fig, '12-051')
