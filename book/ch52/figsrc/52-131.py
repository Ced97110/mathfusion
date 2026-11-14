import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 18, 66, r'$\mathbb{Z}$', 'sujet', 'l'); text(ax, 70, 66, r'restes par 4', 'autre', 'm')
rows = [(r'$5+6=11$', r'$\bar{1}+\bar{2}=\bar{3}$', 'garde +'), (r'$5\times6=30$', r'$\bar{1}\times\bar{2}=\bar{2}$', 'garde ×'), (r'$1$', r'$\bar{1}$', 'garde l’unité')]
for i, (a, b, c) in enumerate(rows):
    y = 52 - i * 18
    box(ax, 4, y - 5, 28, 10, 'sujet', label=a, size='s')
    box(ax, 54, y - 5, 30, 10, 'autre', label=b, size='s')
    arrow(ax, (33, y), (53, y), 'varie')
    text(ax, 43, y + 3, r'$\eta$', 'varie', 'm')
    text(ax, 43, y - 3.2, c, 'resultat', 's')
text(ax, 44, 6, 'trois choses respectées', 'encre', 's')
save(fig, '52-131')
