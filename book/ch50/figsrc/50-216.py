import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, y0, s = 8, 22, 5
for i in range(5):
    for j in range(7):
        box(ax, x0 + s * i, y0 + s * j, 4.2, 4.2, 'sujet', r=0.5, lw=0.5)
text(ax, x0 + 2.1 + 2 * s, y0 + 7 * s + 2.5, '5', 'sujet', 'm')
text(ax, 4, y0 + 3.5 * s, '7', 'sujet', 'm')
text(ax, 60, 52, '5 × 7 = 35 cases', 'sujet', 'm')
text(ax, 60, 43, '47 éléments par case', 'autre', 'm')
text(ax, 60, 34, '35 × 47 = 1 645', 'encre', 'm', weight='bold')
box(ax, 4, 4, 80, 12, 'resultat', label=r'un seul groupe : $\mathbb{Z}/1645\mathbb{Z}$', size='l')
save(fig, '50-216')
