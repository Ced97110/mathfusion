import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bw, bh = 20, 9
def eq(y, op, res, rrole, ww):
    box(ax, 4, y, bw, bh, 'sujet', label=r'$1+x$', size='s')
    text(ax, 4 + bw + 3, y + bh / 2, op, 'encre', 'm')
    box(ax, 4 + bw + 6, y, bw, bh, 'sujet', label=r'$1-x$', size='s')
    text(ax, 4 + 2 * bw + 9, y + bh / 2, '=', 'encre', 'm')
    box(ax, 4 + 2 * bw + 12, y, ww, bh, rrole, label=res, size='s')
box(ax, 1, 33, 86, 27, 'sujet', fill=False, dash=True, lw=0.6)
text(ax, 44, 56, "structure d’espace vectoriel", 'sujet', 's', weight='bold')
eq(37, '+', r'$2$', 'resultat', 22)
box(ax, 1, 3, 86, 27, 'fixe', fill=False, dash=True, lw=0.6)
text(ax, 44, 26, 'autre structure : anneau', 'fixe', 's', weight='bold')
eq(7, r'$\times$', r'$1-x^2$', 'fixe', 22)
save(fig, '58-100')
