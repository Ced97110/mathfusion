import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(40)
f = numberline(ax, 8, 80, 18, -40, 40, step=20, arrow_right=False)
arrow(ax, (f(0), 25), (f(40), 25), 'sujet', lw=1.6)
disc(ax, f(0), 25, 1.2, 'sujet'); disc(ax, f(40), 25, 1.2, 'sujet')
text(ax, f(0), 29, 'O', 'sujet'); text(ax, f(40), 29, 'P', 'sujet')
text(ax, 62, 30, 'r = OP = 40 km', 'sujet', 'm')
c = f(-40) + 1.6
line(ax, [(c - 1.6, 23.4), (c + 1.6, 26.6)], 'limite', lw=1.4)
line(ax, [(c - 1.6, 26.6), (c + 1.6, 23.4)], 'limite', lw=1.4)
text(ax, 3, 32, 'r = −40 : impossible', 'limite', 's', ha='left')
text(ax, 44, 7, 'une distance n’est jamais négative', 'fixe', 's')
save(fig, '39-022')
