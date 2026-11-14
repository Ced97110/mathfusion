import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
def op(x, y, m): ax.plot([x], [y], marker=m, ms=4.5, mew=1.3, color=COL['encre'], zorder=4)
# ligne 1
box(ax, 14, 70, 22, 11, 'fixe', label=r'$x^5$', size='l'); op(44, 75.5, '+'); box(ax, 52, 70, 22, 11, 'sujet', label=r'$x^3$', size='l')
arrow(ax, (44, 68), (44, 60), 'varie')
text(ax, 48, 64, r'$x^5 = x^3 \times x^2$, $x^3 = x^3 \times 1$', 'varie', 's', ha='left') if False else None
text(ax, 47, 64, r'on coupe $5 = 3 + 2$', 'varie', 's', ha='left')
# ligne 2
box(ax, 2, 46, 14, 11, 'sujet', label=r'$x^3$', size='m'); op(19, 51.5, 'x'); box(ax, 22, 46, 14, 11, 'fixe', label=r'$x^2$', size='m')
op(44, 51.5, '+')
box(ax, 52, 46, 14, 11, 'sujet', label=r'$x^3$', size='m'); op(69, 51.5, 'x'); box(ax, 72, 46, 14, 11, 'fixe', label='1', size='m')
arrow(ax, (44, 44), (44, 36), 'varie')
text(ax, 47, 40, r'$x^3$ écrit une fois', 'varie', 's', ha='left')
# ligne 3
box(ax, 8, 22, 22, 11, 'sujet', label=r'$x^3$', size='l'); op(37, 27.5, 'x')
box(ax, 44, 22, 36, 11, 'resultat', label=r'$(x^2 + 1)$', size='l')
text(ax, 44, 12, r'pour $x = 2$ : $32 + 8 = 8 \times 5 = 40$', 'resultat', 's')
save(fig, '14-096')
