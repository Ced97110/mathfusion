import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 0.56
x0 = 4
text(ax, 4, 58, r'$x=5=\mu$ : on compare les termes', 'encre', 'm', ha='left')
box(ax, x0, 42, 125 * s, 9, 'sujet', label=r'$x^3=125$', size='m')
poly(ax, [(x0, 24), (x0 + 15 * s, 24), (x0 + 15 * s, 32), (x0, 32)], 'fixe')
poly(ax, [(x0 + 15 * s, 24), (x0 + 16 * s, 24), (x0 + 16 * s, 32), (x0 + 15 * s, 32)], 'autre')
text(ax, 17, 36, r'les autres : $-3x=-15$ et $1$', 'fixe', 's', ha='left')
text(ax, 17, 28, r'$|-15|+|1|=16$', 'fixe', 'm', ha='left')
line(ax, [(x0 + 16 * s, 21), (x0 + 16 * s, 51)], 'varie', dash=True, lw=0.8)
box(ax, 10, 4, 68, 11, 'resultat', label=r'$125>16$ donc $f(5)\neq 0$', size='m')
save(fig, '69-105')
