import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 4, 63, 5, 4, 'sujet'); text(ax, 11, 65, r'$2\nu$ : plans hyperboliques', 'sujet', 's', ha='left')
box(ax, 4, 56, 5, 4, 'fixe'); text(ax, 11, 58, 'reste : partie anisotrope', 'fixe', 's', ha='left')
data = [(38, r'$n=2,\ \nu=1$', 'HH'), (23, r'$n=3,\ \nu=1$', 'HHX'), (8, r'$n=2,\ \nu=0$', 'XX')]
for y, lab, c in data:
    text(ax, 22, y + 5, lab, 'encre', 's')
    for i, k in enumerate(c): box(ax, 44 + i * 13.5, y, 12, 10, 'sujet' if k == 'H' else 'fixe')
save(fig, '72-127')
