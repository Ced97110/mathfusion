import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 44, 57, 'toutes les règles de prix', 'sujet', 's')
box(ax, 30, 6, 56, 46, 'sujet', label=None, dash=True)
text(ax, 78, 45, r'$V^*$', 'sujet', 'xl')
for k in range(6):
    i, j = k % 3, k // 3
    box(ax, 34 + i * 14, 14 + j * 16, 11, 11, 'varie', label=r'$f$', r=0.6)
box(ax, 2, 20, 18, 22, 'fixe', label=r'$V$', size='xl')
text(ax, 11, 14, 'paniers', 'fixe', 's')
arrow(ax, (20, 31), (30, 31), 'fixe')
text(ax, 44, 3, r'$f\in V^*$', 'encre', 'm')
save(fig, '71-131')
