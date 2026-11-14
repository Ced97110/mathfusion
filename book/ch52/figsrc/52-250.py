import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(54, 3, '3 h : 1 × 2 = 2', 2), (38, 4, '4 h : 3 × 0 = 0', 0), (22, 5, '5 h : 2 × 3 = 6', 1)]
for y, m, s, r in rows:
    text(ax, 2, y, s, 'encre', 's', ha='left')
    for i in range(m):
        box(ax, 40 + i * 6.2, y - 2.5, 5, 5, 'resultat' if i == r else 'fixe')
box(ax, 40 + 5 * 6.2, 19.5, 5, 5, 'limite', dash=True)
arrow(ax, (40 + 5 * 6.2 + 2.5, 25), (40 + 6.2 + 2.5, 25), 'varie', curve=0.35)
text(ax, 40 + 5 * 6.2 + 2.5, 14.5, 'dépasse', 'limite', 's')
text(ax, 2, 12, '6 = 5 + 1 : reste 1', 'varie', 's', ha='left')
save(fig, '52-250')
