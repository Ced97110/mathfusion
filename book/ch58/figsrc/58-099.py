import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 45, 'un vecteur est un polynôme', 'sujet', 's', weight='bold')
bw, bh = 22, 9
def eq(y, items):
    x = 3
    for kind, s, role in items:
        if kind == 'b':
            box(ax, x, y, bw, bh, role, label=s, size='s'); x += bw
        else:
            text(ax, x + 3, y + bh / 2, s, 'encre', 'm'); x += 6
eq(26, [('b', r'$2+3x$', 'sujet'), ('t', '+', 0), ('b', r'$1+4x$', 'sujet'), ('t', '=', 0), ('b', r'$3+7x$', 'resultat')])
x = 3
text(ax, 8, 12.5, r'$5\,\times$', 'encre', 'm')
box(ax, 15, 8, bw, bh, 'sujet', label=r'$2+3x$', size='s')
text(ax, 15 + bw + 3, 12.5, '=', 'encre', 'm')
box(ax, 15 + bw + 6, 8, 26, bh, 'varie', label=r'$10+15x$', size='s')
save(fig, '58-099')
