import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 80, 28, -4, 4, arrow_right=False, labels=False)
text(ax, f(0), 24, '0', 'fixe', 's')
disc(ax, f(-3), 28, 3, 'sujet', label='−3', size='s'); disc(ax, f(3), 28, 3, 'sujet', label='3', size='s')
arrow(ax, (f(-3), 31), (f(3), 31), 'varie', curve=-0.35); text(ax, 44, 44, '3 divise −3 : −3 = 3 × (−1)', 'varie', 's')
arrow(ax, (f(3), 25), (f(-3), 25), 'varie', curve=-0.35); text(ax, 44, 11, '−3 divise 3 : 3 = (−3)×(−1)', 'varie', 's')
box(ax, 12, 49, 64, 9, 'limite', label='3 ≠ −3 : antisymétrie fausse', size='s')
save(fig, '79-025')
