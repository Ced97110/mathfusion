import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
X0, CW, CH = 4.0, 5.0, 7.0
def cells(y, n, role):
    for i in range(n):
        box(ax, X0 + i * CW, y, CW - 0.6, CH, role, r=0.4, lw=0.7)
text(ax, X0, 72, r'$G$ : 12 éléments, $p = 2$', 'encre', 's', ha='left')
cells(60, 12, 'fixe')
text(ax, X0, 49, r'$k = 1$ : $2^1 = 2$ éléments', 'sujet', 's', ha='left')
cells(40, 2, 'sujet')
text(ax, X0, 29, r'$k = 2$ : $2^2 = 4$ éléments', 'autre', 's', ha='left')
cells(18, 4, 'autre')
# crochets verticaux : Sylow I couvre k = 1 et k = 2, Cauchy seulement k = 1
xs, xc = 69.0, 80.0
for x, y0, y1, role in ((xs, 18, 47, 'fixe'), (xc, 40, 47, 'sujet')):
    line(ax, [(x - 1.5, y0), (x, y0), (x, y1), (x - 1.5, y1)], role, lw=1.0)
text(ax, xs, 51, 'Sylow I', 'fixe', 's')
text(ax, xc, 51, 'Cauchy', 'sujet', 's')
save(fig, '50-056')
