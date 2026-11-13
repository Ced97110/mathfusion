import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
k = 0.01                                    # mm par mètre
bs, h = 5450.73 * k, 1975.55 * k
box(ax, 2, 55, 84, 9, 'sujet', label=r'$h = BS\,\sin\beta$', size='m')
box(ax, 4, 38, bs, 7, 'varie', label='BS ≈ 5 451 m', size='s')
box(ax, 4, 20, h, 7, 'resultat', label='h ≈ 1 976 m', size='s')
arrow(ax, (12, 37), (12, 28), 'varie')
text(ax, 15, 32.5, '× 0,36244', 'varie', 's', ha='left', weight='bold')
text(ax, 44, 12, 'sin 21,25° ≈ 0,36244', 'sujet', 's')
text(ax, 44, 6, 'nombre sans unité : h < BS', 'fixe', 's')
save(fig, '38-043')
