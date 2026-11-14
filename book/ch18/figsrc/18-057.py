import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = (6, 34, 62)
def row(y, labs, roles, head, hrole):
    text(ax, 44, y + 14, head, hrole, 'm', weight='bold')
    for x, l, r in zip(xs, labs, roles): box(ax, x, y, 20, 9, r, label=l, r=0.5)
    brace(ax, xs[1], xs[2] + 20, y + 9.5, roles[1] if hrole != 'limite' else 'limite', down=False, depth=1.4)
row(46, (r'$x^2$', r'$2kx$', r'$k^2$'), ('sujet', 'varie', 'varie'), r'$(x+k)^2$ : même $k$ au milieu et au bout', 'encre')
row(25, (r'$x^2$', r'6$x$ = 2 × 3 ×$x$', '9 = 3²'), ('sujet', 'resultat', 'resultat'), r'$k$ = 3 : trinôme carré parfait', 'resultat')
row(4, (r'$x^2$', r'5$x$ : $k$ = 2,5', r'6 ≠ $k^2$ = 6,25'), ('sujet', 'limite', 'limite'), r'$x^2+5x+6$ : pas un carré', 'limite')
save(fig, '18-057')
