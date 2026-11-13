import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
EM = ' '
def mat(cx, cy, r1, r2, role, hw=7):
    text(ax, cx, cy + 3.2, r1, role, 's'); text(ax, cx, cy - 3.2, r2, role, 's')
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.4, cy + 7), (x, cy + 7), (x, cy - 7), (x - s * 1.4, cy - 7)], role, lw=0.9)
def dot(x, y):
    disc(ax, x, y, 0.7, 'encre')
def eq(x, y):
    line(ax, [(x - 1.5, y + 0.8), (x + 1.5, y + 0.8)], 'encre', 1.0); line(ax, [(x - 1.5, y - 0.8), (x + 1.5, y - 0.8)], 'encre', 1.0)
y = 33
xs = [11, 31, 52, 77]
mat(xs[0], y, '0' + EM + '1', '1' + EM + '0', 'varie')
mat(xs[1], y, '0' + EM + '−1', '1' + EM + '0', 'sujet')
mat(xs[2], y, '0' + EM + '1', '1' + EM + '0', 'varie')
mat(xs[3], y, '0' + EM + '1', '−1' + EM + '0', 'autre')
dot(21, y); dot(41.5, y); eq(64.5, y)
text(ax, xs[0], y + 11, r'$\Delta^{-1}$', 'varie', 'm'); text(ax, xs[1], y + 11, r'$\rho(i)$', 'sujet', 'm')
text(ax, xs[2], y + 11, r'$\Delta$', 'varie', 'm'); text(ax, xs[3], y + 11, r'$\Delta^{-1}\rho(i)\,\Delta$', 'autre', 'm')
text(ax, xs[0], y - 12, 'lignes', 'varie', 's'); text(ax, xs[1], y - 12, r'base $1,\ i$', 'sujet', 's')
text(ax, xs[2], y - 12, 'colonnes', 'varie', 's'); text(ax, xs[3], y - 12, r'base $i,\ 1$', 'autre', 's')
brace(ax, xs[1] - 8, xs[2] + 8, y - 17, 'sujet', label=r"d'abord $\rho(i)\Delta$")
save(fig, '77-032')
