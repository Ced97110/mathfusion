import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for i, v in enumerate([7, 6, 4]): box(ax, 22 + i * 16, 64, 12, 9, 'fixe', label=str(v))
rows = [(r'$\sum$', 'autre', 'additionne les 3 : 17'), (r'$\times$', 'fixe', 'multiplie 2 : 7 × 6 = 42'),
        (r'$\prod$', 'sujet', 'multiplie les 3 : 168')]
for i, (s, r, d) in enumerate(rows):
    y = 46 - i * 17
    text(ax, 12, y, s, r, 'xl'); box(ax, 22, y - 6, 62, 12, r, label=d, size='m')
    arrow(ax, (17, y), (21.5, y), r)
save(fig, '73-175')
