import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'$3x + 2x = 5x$', 'sujet', 'l', weight='bold')
text(ax, 14, 61, r'$x$', 'varie', 'm')
text(ax, 56, 61, 'les deux côtés', 'sujet', 's')
for i, (v, r) in enumerate([('1', '5 = 5'), ('2', '10 = 10'), ('10', '50 = 50')]):
    y = 44 - i * 14
    box(ax, 4, y, 20, 10, 'varie', label=v, size='m')
    box(ax, 30, y, 52, 10, 'resultat', label=r, size='m')
box(ax, 8, 2, 72, 8, 'resultat', label='vraie pour toutes les valeurs', size='s')
save(fig, '16-127')
