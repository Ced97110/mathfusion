import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
xs = (2, 36, 70)
boxes = ((r'$m = 2$', 'sujet', 'message'), (r"$x' = 32$", 'varie', 'message signé'), (r'$y = 43$', 'resultat', 'envoyé'))
for x, (l, r, c) in zip(xs, boxes):
    box(ax, x, 30, 16, 11, r, label=l)
    text(ax, x + 8, 46, c, r, 's')
for xa, xb, p, md, who, r in ((18.5, 35.5, r'$2^{29}$', 'mod 91', 'clé de Bob', 'varie'),
                              (52.5, 69.5, r'$32^{3}$', 'mod 55', 'clé d’Alice', 'autre')):
    arrow(ax, (xa, 35.5), (xb, 35.5), r)
    xm = (xa + xb) / 2
    text(ax, xm, 40.5, p, r, 's')
    text(ax, xm, 30.5, md, r, 's')
    text(ax, xm, 22, who, r, 's', weight='bold')
text(ax, 44, 10, 'd’abord Bob signe, puis il chiffre', 'fixe', 's')
save(fig, '53-154')
