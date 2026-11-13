import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = (2, 36, 70)
boxes = ((r'$43$', 'sujet', 'reçu'), (r'$32$', 'varie', 'message signé'), (r'$2$', 'resultat', 'message'))
for x, (l, r, c) in zip(xs, boxes):
    box(ax, x, 36, 16, 11, r, label=l)
    text(ax, x + 8, 52, c, r, 's')
for xa, xb, p, md, who, step, r in ((18.5, 35.5, r'$43^{27}$', 'mod 55', 'clé d’Alice', 'défait le chiffrement', 'autre'),
                              (52.5, 69.5, r'$32^{5}$', 'mod 91', 'clé de Bob', 'défait la signature', 'varie')):
    arrow(ax, (xa, 41.5), (xb, 41.5), r)
    xm = (xa + xb) / 2
    text(ax, xm, 46.5, p, r, 's')
    text(ax, xm, 36.5, md, r, 's')
    text(ax, xm, 28, who, r, 's', weight='bold')
    text(ax, xm, 23.5, step, r, 's')
text(ax, 78, 28, 'stop', 'resultat', 's', weight='bold')
save(fig, '53-155')
