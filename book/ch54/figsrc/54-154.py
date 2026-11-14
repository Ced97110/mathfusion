import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 16, 60, 12, 10, 'fixe', label=r'$f$', size='l')
text(ax, 34, 65, '=', 'fixe', 'l')
box(ax, 40, 60, 10, 10, 'fixe', label=r'$q$', size='l')
box(ax, 54, 60, 10, 10, 'fixe', label=r'$g$', size='l')
text(ax, 69, 65, '+', 'fixe', 'l')
box(ax, 74, 60, 10, 10, 'sujet', label=r'$r$', size='l')
text(ax, 79, 55, 'reste', 'sujet', 's')
text(ax, 44, 44, r'$f=x^3-2x^2+4$ divisé par $g=x-1$', 'fixe', 's')
# barres de degré
y0, u = 14, 14
ax.add_patch(Rectangle((28, y0), 8, u, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=2))
ax.plot([48, 60], [y0, y0], color=COL['sujet'], lw=2.0, zorder=3, solid_capstyle='round')
text(ax, 32, y0 + u + 4, r'$\deg g=1$', 'fixe', 's')
text(ax, 54, y0 + 4, r'$\deg r=0$', 'sujet', 's')
text(ax, 44, 4, r'$r=3$ : $\deg r<\deg g$', 'resultat', 'm')
save(fig, '54-154')
