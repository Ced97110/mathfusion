import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'vecteur $(1, i)$, non nul', 'encre', 'm')
f = numberline(ax, 14, 62, 26, -1, 1, arrow_right=False)
arrow(ax, (f(0), 60), (f(1), 60), 'sujet'); text(ax, (f(0) + f(1)) / 2, 64.5, r'$1^2$ = 1', 'sujet', 's')
arrow(ax, (f(1), 48), (f(0), 48), 'varie'); text(ax, (f(0) + f(1)) / 2, 43.5, r'$i^2$ = −1', 'varie', 's')
line(ax, [(f(1), 60), (f(1), 28)], 'fixe', dash=True); line(ax, [(f(0), 48), (f(0), 28)], 'fixe', dash=True)
disc(ax, f(0), 26, 2, 'limite'); text(ax, f(0), 12, r'total : 1 + (−1) = 0', 'limite', 's')
save(fig, '75-010')
