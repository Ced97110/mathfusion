import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
box(ax, 2, 50, 54, 26, 'autre'); text(ax, 29, 70, r'$ax+by=c$', 'autre', 'l'); text(ax, 29, 57, r'$2x+3y=12$', 'autre', 'm')
box(ax, 60, 52, 26, 22, 'autre', label=r'$b=3$', size='l')
text(ax, 73, 46, r'multiplie $y$', 'autre', 's')
box(ax, 2, 6, 54, 26, 'sujet'); text(ax, 29, 26, r'$y=mx+b$', 'sujet', 'l'); text(ax, 29, 13, r'$y=-\frac{2}{3}x+4$', 'sujet', 'm')
box(ax, 60, 8, 26, 22, 'sujet', label=r'$b=4$', size='l')
text(ax, 73, 2.5, 'nombre seul', 'sujet', 's')
text(ax, 73, 40, r'$\neq$', 'limite', 'xl')
text(ax, 29, 41, 'même droite', 'fixe', 's')
save(fig, '19-087')
