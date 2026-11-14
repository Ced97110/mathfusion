import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(58)
text(ax, 20, 52, 'lu : « tangente moins un »', 'autre', 's')
text(ax, 20, 47.5, 'calculatrices, livres anglais', 'autre', 's'); text(ax, 68, 47.5, 'ce livre', 'sujet', 's')
box(ax, 4, 31, 32, 12, 'autre', label=r'$\tan^{-1}$', size='l')
box(ax, 52, 31, 32, 12, 'sujet', label='arctan', size='l')
text(ax, 44, 37, '=', 'encre', 'l', weight='bold')
box(ax, 22, 6, 44, 10, 'resultat', label='du rapport à l’angle', size='s')
arrow(ax, (20, 30.5), (32, 16.5), 'varie'); arrow(ax, (68, 30.5), (56, 16.5), 'varie')
save(fig, '25-080')
