import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = 2.2; x0 = 14
def row(y, n, keep, lab):
    for i in range(n):
        r = 'resultat' if i < keep else 'varie'
        ax.add_patch(Rectangle((x0+i*c, y), c, 5, ec=COL[r], fc=FILL[r], lw=0.5, zorder=2))
    text(ax, 7, y+2.5, lab, 'encre', 'l')
text(ax, 44, 57, '1 case = 1/16', 'fixe', 's')
row(44, 16, 16, r'$P$')
text(ax, x0+8*c, 38, r'$1^{2}-0^{2}=1$', 'resultat', 'm')
row(24, 25, 16, r'$\eta P$')
text(ax, x0+12.5*c, 18, r'$\frac{25}{16}-\frac{9}{16}=1$', 'encre', 'm')
text(ax, x0+20.5*c, 33, '9 cases ôtées', 'varie', 's')
text(ax, 44, 6, 'même carré : 1', 'resultat', 'l')
save(fig, '72-096')
