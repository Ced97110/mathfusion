import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
k = 0.0073                                  # mm par mètre : 5 451 m -> 39,8 mm
d1, d2 = 1000 * k, 2000 * k
b1, b2 = 5450.73 * k, 10901.46 * k
box(ax, 2, 68, 84, 9, 'sujet', label=r'$BS = d\,\sin\alpha\,/\,\sin(\beta-\alpha)$', size='s')
# ligne 1 : d = 1 000 m
y1 = 53
box(ax, 4, y1, d1, 5, 'fixe', label='d', size='s')
text(ax, 4 + d1 + 2, y1 + 2.5, '= 1 000 m', 'fixe', 's', ha='left', weight='bold')
box(ax, 4, y1 - 10, b1, 6, 'resultat', label='BS ≈ 5 451 m', size='s')
arrow(ax, (7, y1 - 0.6), (7, y1 - 3.4), 'varie')
# ligne 2 : d = 2 000 m
y2 = 29
box(ax, 4, y2, d2, 5, 'fixe', label='d', size='s')
text(ax, 4 + d2 + 2, y2 + 2.5, '= 2 000 m', 'fixe', 's', ha='left', weight='bold')
box(ax, 4, y2 - 10, b2, 6, 'resultat', label='BS ≈ 10 901 m', size='s')
arrow(ax, (7, y2 - 0.6), (7, y2 - 3.4), 'varie')
text(ax, 10, y1 - 1.9, '× 5,451', 'varie', 's', ha='left', weight='bold')
text(ax, 10, y2 - 1.9, '× 5,451', 'varie', 's', ha='left', weight='bold')
text(ax, 44, 7, '5,451 = sin 18° / sin 3,25°', 'sujet', 's')
save(fig, '38-032')
