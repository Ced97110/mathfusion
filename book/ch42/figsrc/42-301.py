import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 26, 60, 'bijections de $S$', 'sujet', 'm')
box(ax, 4, 41, 44, 10, 'fixe', label='composée : bijection', size='s')
box(ax, 4, 26, 44, 11, 'varie', label='inverse : bijection', size='s', lw=1.8, weight='bold')
box(ax, 4, 12, 44, 10, 'fixe', label='identité : bijection', size='s')
for y, ye, role, lw in ((46, 38, 'fixe', 0.9), (31.5, 32, 'varie', 2.0), (17, 26, 'fixe', 0.9)):
    arrow(ax, (49, y), (59.4, ye), role, lw=lw)
box(ax, 60, 22, 26, 20, 'resultat', label='groupe', size='m', weight='bold')
text(ax, 44, 4, 'sans inverse, pas de groupe', 'varie', 'm', weight='bold')
save(fig, '42-301')
