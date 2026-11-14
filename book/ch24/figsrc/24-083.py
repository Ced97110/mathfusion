import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, a, ra, op, b, rb, c, rc, wa, wb, wc):
    x = 3.0
    box(ax, x, y, wa, 8, ra, label=a, size='s'); x += wa + 1
    text(ax, x + 2, y + 4, op, 'varie', 'l'); x += 5
    box(ax, x, y, wb, 8, rb, label=b, size='s'); x += wb + 1
    text(ax, x + 2, y + 4, '=', 'encre', 'l'); x += 5
    box(ax, x, y, wc, 8, rc, label=c, size='s')
text(ax, 3, 59, r'tour 1 : $y$ disparaît', 'varie', 's', ha='left')
row(46, r'$x + y + z = 9$', 'sujet', r'$-$', r'$2x + y = 8$', 'sujet', r'$-x + z = 1$', 'varie', 26, 22, 21)
arrow(ax, (20, 45), (20, 35), 'fixe')
text(ax, 3, 33, r'tour 2 : $x$ disparaît', 'varie', 's', ha='left')
row(20, r'$-x + z = 1$', 'varie', r'$+$', r'$x + 2z = 11$', 'sujet', r'$3z = 12$', 'resultat', 22, 24, 21)
arrow(ax, (72, 19), (72, 11), 'resultat')
box(ax, 62, 2, 20, 8, 'resultat', label=r'$z = 4$', size='s')
save(fig, '24-083')
