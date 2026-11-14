import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [(15, r'$\mathbb{Z}$', r'$2 \times 3$', r'$= 6$'),
        (44, r'polynômes', r'$x(x+1)$', r'$= x^2 + x$'),
        (73, r'$\mathbb{Z}[\sqrt{2}]$', r'$(1+\sqrt{2})(2+3\sqrt{2})$', r'$= 8 + 5\sqrt{2}$')]
for x, name, fac, res in cols:
    box(ax, x - 13.5, 6, 27, 48, 'sujet')
    text(ax, x, 48, name, 'sujet', 'm', weight='bold')
    text(ax, x, 38, fac, 'encre', 's')
    text(ax, x, 30, res, 'resultat', 's')
    arrow(ax, (x, 35), (x, 33), 'fixe', lw=0.6) if False else None
    text(ax, x, 18, r'$\neq 0$', 'resultat', 'l')
    text(ax, x, 11, 'produit non nul', 'resultat', 's') if False else None
save(fig, '51-105')
