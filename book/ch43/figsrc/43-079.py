import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 6, 60, 22, 14, 'sujet', label=r'$\mathbb{Z}$', size='l'); text(ax, 17, 55, 'tous les entiers', 'sujet', 's')
text(ax, 33, 67, '/', 'encre', 'l', weight='bold')
box(ax, 38, 60, 26, 14, 'varie', label=r'$12\mathbb{Z}$', size='l'); text(ax, 51, 55, 'quelle horloge', 'varie', 's')
cx, cy, R = 44, 26, 17
for i in range(12):
    a = math.radians(90 - 30 * i)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    disc(ax, x, y, 3.2, 'resultat')
    if i % 3 == 0: text(ax, x, y, r'$\bar{%d}$' % i, 'resultat', 's')
text(ax, 72, 26, '12 positions', 'resultat', 's')
text(ax, 16, 26, '12 classes', 'resultat', 's')
save(fig, '43-079')
