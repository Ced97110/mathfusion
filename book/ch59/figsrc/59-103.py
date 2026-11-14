import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 3, 10, 82, 40, 'sujet', fill=True, r=2)
text(ax, 44, 55, '(2) : les multiples de 2', 'sujet', 's')
box(ax, 50, 14, 32, 32, 'autre', fill=True, r=2)
text(ax, 66, 41, '(10)', 'autre', 's', weight='bold')
for i, n in enumerate((2, 4, 6, 8)):
    text(ax, 12 + i * 9, 36, str(n), 'sujet', 's')
for i, n in enumerate((12, 14)):
    text(ax, 12 + i * 9, 24, str(n), 'sujet', 's')
for i, n in enumerate((10, 20, 30)):
    text(ax, 56 + i * 9, 28, str(n), 'autre', 's')
text(ax, 44, 4, '(2) ⊇ (10)', 'encre', 'm', weight='bold')
save(fig, '59-103')
