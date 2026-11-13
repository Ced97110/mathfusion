import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'primitif : contenu égal à 1', 'sujet', 'm', weight='bold')
def row(y, a, ca, ra, b, cb, rb, prod, cp, rp, verdict, rv):
    box(ax, 2, y, 19, 14, ra, label=a + '\ncontenu ' + ca, size='s')
    text(ax, 24, y + 7, '×', 'encre', 'l')
    box(ax, 27, y, 19, 14, rb, label=b + '\ncontenu ' + cb, size='s')
    text(ax, 49, y + 7, '=', 'encre', 'l')
    box(ax, 52, y, 34, 14, rp, label=prod + '\ncontenu ' + cp, size='s')
    text(ax, 69, y - 4.5, verdict, rv, 's')
row(50, r'$3+4x$', '1', 'sujet', r'$x+1$', '1', 'sujet', r'$3+7x+4x^2$', '1', 'sujet', 'produit primitif', 'resultat')
row(18, r'$2+2x$', '2', 'autre', r'$x+1$', '1', 'sujet', r'$2+4x+2x^2$', '2', 'limite', 'produit pas primitif', 'limite')
save(fig, '54-218')
