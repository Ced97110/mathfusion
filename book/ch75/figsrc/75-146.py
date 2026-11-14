import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def row(y, z, lab, ro, cap, capr):
    text(ax, 2, y + 15, cap, capr, 's', ha='left')
    box(ax, 2, y, 16, 10, capr, label=z)
    arrow(ax, (19, y + 5), (35, y + 5), 'varie'); text(ax, 27, y + 8.6, lab, 'varie', 's')
    box(ax, 36, y, 14, 10, 'varie', label='25')
    arrow(ax, (51, y + 5), (67, y + 5), 'varie'); text(ax, 59, y + 8.6, r'$\sqrt{\ }$', 'varie', 's')
    box(ax, 68, y, 18, 10, 'resultat', label='5', weight='bold')
row(32, r'$3+4i$', r'$\times\,\bar z$', 'resultat', 'complexe', 'sujet')
row(6, r'$-5$', r'$\times\,(-5)$', 'resultat', 'réel', 'autre')
save(fig, '75-146')
