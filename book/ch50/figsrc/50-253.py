import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60.5, 'ordres impairs : pas simples', 'limite', 's')
for i, n in enumerate(['15', '21', '99', '1645']):
    x = 4 + 21 * i
    box(ax, x, 38, 17, 12, 'fixe'); text(ax, x + 8.5, 54, n, 'encre', 'm', weight='bold')
    line(ax, [(x + 1, 39), (x + 16, 49)], 'limite', lw=1.2); line(ax, [(x + 1, 49), (x + 16, 39)], 'limite', lw=1.2)
arrow(ax, (44, 36), (44, 29), 'varie')
box(ax, 8, 8, 72, 20, 'resultat')
text(ax, 44, 22.5, 'groupe simple non premier', 'resultat', 's')
text(ax, 44, 14, r'$\Rightarrow$ ordre pair', 'resultat', 'l', weight='bold')
text(ax, 44, 3.5, 'preuve : plus de 250 pages', 'fixe', 's')
save(fig, '50-253')
