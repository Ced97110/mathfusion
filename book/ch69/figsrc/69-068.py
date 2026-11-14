import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
X0, X1 = 34, 82
XM = (X0 + X1) / 2
text(ax, X0, 54, r'en $0$', 'encre', 's')
text(ax, X1, 54, r'en $2$', 'encre', 's')
# (label, y, valeur en 0, valeur en 2, signe change au milieu)
rows = [(r'$x-1$', 41, r'$-1$', r'$1$', True),
        (r'$x+2$', 30, r'$2$', r'$4$', False),
        (r'$x^2+1$', 19, r'$1$', r'$5$', False),
        (r'produit $f$', 5, r'$-2$', r'$20$', True)]
for lab, y, v0, v2, change in rows:
    text(ax, 3, y + 4, lab, 'encre', 'm', ha='left')
    if change:
        box(ax, X0, y, XM - X0, 8, 'varie')
        box(ax, XM, y, X1 - XM, 8, 'resultat')
    else:
        box(ax, X0, y, X1 - X0, 8, 'resultat')
    text(ax, X0 + 1.5, y + 4, v0, 'encre', 's', ha='left')
    text(ax, X1 - 1.5, y + 4, v2, 'encre', 's', ha='right')
line(ax, [(XM, 50), (XM, 4)], 'fixe', dash=True)
save(fig, '69-068')
