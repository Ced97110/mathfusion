import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
pitch = 1.272 * 11 * 25.4 / 72
xc = 50
text(ax, 44, 53, 'chaque position se calcule seule', 'encre', 'm')
bx = xc + pitch
poly(ax, [(bx - 2.5, 12), (bx + 2.5, 12), (bx + 2.5, 49), (bx - 2.5, 49)], 'varie')
sp = lambda w: '  '.join(w)
text(ax, xc, 42, sp('0011001'), 'sujet', 'xl')
text(ax, xc, 30, sp('0000100'), 'autre', 'xl')
line(ax, [(30, 24), (70, 24)], 'fixe')
text(ax, xc, 17, sp('0011101'), 'resultat', 'xl')
text(ax, 6, 42, r'$x$', 'sujet', 'l', ha='left')
text(ax, 6, 30, r'$+\ y$', 'autre', 'l', ha='left')
text(ax, 6, 17, r'$x+y$', 'resultat', 'l', ha='left')
text(ax, bx, 6, 'position 5 : 0 + 1 = 1', 'varie', 's')
save(fig, '68-026')
