import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'dans $\mathbb{Z}/6\mathbb{Z}$', 'encre', 'm')
for n in range(6):
    r = 'varie' if n == 3 else ('sujet' if n == 1 else 'fixe')
    disc(ax, 12 + n * 12.8, 32, 5, r, label=r'$\bar{%d}$' % n, size='m')
text(ax, 12 + 3 * 12.8, 46, r'$\bar{3}\times\bar{3}=\bar{9}=\bar{3}$', 'varie', 's')
arrow(ax, (12 + 3 * 12.8, 44), (12 + 3 * 12.8, 38), 'varie')
text(ax, 12 + 12.8, 20, 'l’unité', 'sujet', 's'); arrow(ax, (12 + 12.8, 23), (12 + 12.8, 27), 'sujet')
text(ax, 12 + 3 * 12.8, 20, r'pas l’unité', 'limite', 's')
text(ax, 44, 8, r'$\bar{3}\bar{3}=\bar{3}$ sans que $\bar{3}=\bar{1}$', 'limite', 's')
save(fig, '52-139')
