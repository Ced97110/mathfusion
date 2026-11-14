import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 61, r'$t = \frac{120}{v}$', 'sujet', 'xl')
text(ax, 17, 61, 'temps (h)', 'sujet', 's'); text(ax, 71, 61, 'vitesse (km/h)', 'varie', 's')
for i, (v, t) in enumerate([(40, 3), (30, 4)]):
    y = 34 - i * 20
    box(ax, 2, y, 22, 11, 'varie', label=rf'$v = {v}$')
    box(ax, 33, y, 26, 11, 'sujet', label=rf'$t = \frac{{120}}{{{v}}}$', size='m')
    box(ax, 68, y, 18, 11, 'resultat', label=rf'$t = {t}$')
    arrow(ax, (24.5, y + 5.5), (32.5, y + 5.5), 'varie'); arrow(ax, (59.5, y + 5.5), (67.5, y + 5.5), 'resultat')
text(ax, 28, 50, 'on remplace v', 'varie', 's'); text(ax, 63.5, 50, 'on divise', 'resultat', 's')
save(fig, '21-002')
