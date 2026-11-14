import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 4 + 3 == 7 and 7 - 4 == 3

fig, ax = canvas(62)
text(ax, 44, 58, r'$4 + b \equiv 7$, donc $b = 3$', 'resultat', 'l', weight='bold')
f = numberline(ax, 8, 68, 22, 3, 8, step=1, arrow_right=True)
box(ax, f(4) - 6, 38, 12, 12, 'sujet', label='E\n4', size='s')
box(ax, f(7) - 6, 38, 12, 12, 'resultat', label='H\n7', size='s')
arrow(ax, (f(4), 38), (f(4), 23.5), 'sujet', lw=0.8)
arrow(ax, (f(7), 38), (f(7), 23.5), 'resultat', lw=0.8)
arrow(ax, (f(4) + 1.5, 36), (f(7) - 1.5, 36), 'varie', curve=0.0)
text(ax, (f(4) + f(7)) / 2, 40, r'$+\,b$', 'varie', 'm')
text(ax, 44, 8, 'hypothèse : E est devenu H,\ncar H est la plus fréquente', 'fixe', 's')
save(fig, '53-067')
