import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [(68, ('(1, 0)', 'sujet'), ('(0, 1)', 'sujet'), 'départ : la base'),
        (40, ('(1, 1)', 'varie'), ('(0, 1)', 'sujet'), '(1, 1) remplace (1, 0)'),
        (12, ('(1, 1)', 'resultat'), ('(1, 2)', 'varie'), '(1, 2) remplace (0, 1)')]
for y, a, b, cap in rows:
    box(ax, 4, y, 24, 10, a[1], label=a[0])
    box(ax, 32, y, 24, 10, b[1], label=b[0])
    text(ax, 60, y + (7 if y < 20 else 5), cap, 'varie' if y < 60 else 'fixe', 's', ha='left')
text(ax, 60, 14, 'engendrent le plan', 'resultat', 's', ha='left')
arrow(ax, (16, 67), (16, 52), 'varie', lw=1.2)
text(ax, 19, 59.5, '(1, 0) = (1, 1) − (0, 1)', 'varie', 's', ha='left')
arrow(ax, (44, 39), (44, 24), 'varie', lw=1.2)
text(ax, 47, 31.5, '(0, 1) = (1, 2) − (1, 1)', 'varie', 's', ha='left')
save(fig, '58-296')
