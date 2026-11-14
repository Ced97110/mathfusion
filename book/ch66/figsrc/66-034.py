import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'écrit en entier', 'fixe', 's')
xs = [10 + i * 17 for i in range(5)]
for i, x in enumerate(xs):
    box(ax, x - 5, 42, 10, 10, 'fixe', label=str(i + 1))
    if i < 4: text(ax, x + 8.5, 47, r'$\times$', 'varie', 'm')
arrow(ax, (44, 40), (44, 31), 'varie')
text(ax, 47, 35.5, 'en un seul signe', 'varie', 's', ha='left')
box(ax, 10, 8, 68, 20, 'sujet')
text(ax, 22, 18, r'$\prod$', 'sujet', 'xl')
text(ax, 58, 22, 'les facteurs : la liste', 'sujet', 's')
text(ax, 58, 14, r'$1,\ 2,\ 3,\ 4,\ 5$', 'sujet', 'm')
save(fig, '66-034')
