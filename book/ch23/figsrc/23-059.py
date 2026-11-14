import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 28, 28, 13, 'sujet', label=r'$-4\pm\sqrt{136}$')
box(ax, 50, 48, 36, 13, 'resultat', label=r'$-4+\sqrt{136}$'); box(ax, 50, 8, 36, 13, 'resultat', label=r'$-4-\sqrt{136}$')
arrow(ax, (30.5, 38), (49.5, 54), 'varie'); arrow(ax, (30.5, 31), (49.5, 15), 'varie')
text(ax, 38, 51, 'avec plus', 'varie', 's'); text(ax, 38, 18, 'avec moins', 'varie', 's')
text(ax, 16, 20, 'deux calculs', 'varie', 's')
save(fig, '23-059')
