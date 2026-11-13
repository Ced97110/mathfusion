import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 20, 54, r'$M$ : riz d’abord', 'sujet', 'm')
text(ax, 68, 54, r'$N$ : lentilles d’abord', 'autre', 'm')
rows = [(34, '(2, 1)', '(1, 2)'), (10, '(2, 1) + (2, 1) = (4, 2)', '(1, 2) + (1, 2) = (2, 4)')]
for y, a, b in rows:
    w = 28 if len(a) < 10 else 40
    if len(a) < 10:
        box(ax, 10, y, 22, 10, 'sujet', label=a)
        box(ax, 56, y, 22, 10, 'autre', label=b)
        arrow(ax, (33, y + 5), (55, y + 5), 'varie', both=True)
        text(ax, 44, y + 9, 'échange des cases', 'varie', 's')
    else:
        box(ax, 2, y, 36, 10, 'sujet', label=a, size='s')
        box(ax, 50, y, 36, 10, 'autre', label=b, size='s')
        arrow(ax, (39, y + 5), (49, y + 5), 'varie', both=True)
save(fig, '58-053')
