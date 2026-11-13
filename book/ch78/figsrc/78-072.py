import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def pair(x0, a, b, r):
    box(ax, x0, 30, 9, 9, r, label=a); box(ax, x0 + 9, 30, 9, 9, r, label=b)
pair(2, '1', '2', 'sujet'); pair(28, '2', '3', 'autre'); pair(56, '−4', '7', 'resultat')
text(ax, 11, 43.5, '$x$', 'sujet'); text(ax, 37, 43.5, '$y$', 'autre'); text(ax, 65, 43.5, '$z$', 'resultat')
text(ax, 24, 34.5, r'$\times$'); text(ax, 51, 34.5, '=')
text(ax, 44, 21, '1er nombre : 1×2 − 2×3 = −4', 'resultat', 's')
text(ax, 44, 12, '2e nombre : 1×3 + 2×2 = 7', 'resultat', 's')
save(fig, '78-072')
