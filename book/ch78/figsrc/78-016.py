import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
for y0, name, ex, res in [(70, 'produit de deux nombres', r'$2\times3$', '6'),
                          (55, 'produit scalaire', r'$u\cdot v$', '2')]:
    text(ax, 3, y0 + 10, name, 'fixe', 's', ha='left')
    text(ax, 14, y0 + 3, ex, 'encre', 'm')
    arrow(ax, (24, y0 + 3), (34, y0 + 3), 'fixe')
    box(ax, 38, y0 - 2, 12, 10, 'fixe', label=res)
    text(ax, 62, y0 + 3, 'rend un nombre', 'fixe', 's', ha='left')
text(ax, 3, 44, 'produit vectoriel', 'sujet', 's', ha='left')
o = (28, 6); k = 9
P = lambda a, b, c: iso(a, b, c, o, k)
poly(ax, [P(0, 0, 0), P(2, 0, 0), P(3, 1.5, 0), P(1, 1.5, 0)][::1] if False else [P(0, 0, 0), P(2, 0, 0), P(3, 1.5, 0), P(1, 1.5, 0)], 'fixe')
arrow(ax, P(0, 0, 0), P(2, 0, 0), 'sujet', lw=1.6)
arrow(ax, P(0, 0, 0), P(1, 1.5, 0), 'varie', lw=1.6)
arrow(ax, P(0, 0, 0), P(0, 0, 3), 'resultat', lw=2.0)
text(ax, P(2, 0, 0)[0] + 2, P(2, 0, 0)[1] - 3, r'$u$ (2 ; 0 ; 0)', 'sujet', 's', ha='left')
text(ax, P(1, 1.5, 0)[0] - 2, P(1, 1.5, 0)[1] + 3, r'$v$ (1 ; 1,5 ; 0)', 'varie', 's', ha='right')
text(ax, P(0, 0, 3)[0] + 3, P(0, 0, 3)[1], r'$u\times v$ = (0 ; 0 ; 3)', 'resultat', 's', ha='left')
text(ax, P(0, 0, 3)[0] + 3, P(0, 0, 3)[1] - 5, 'rend une flèche', 'resultat', 's', ha='left')
save(fig, '78-016')
