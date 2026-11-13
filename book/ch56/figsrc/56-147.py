import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def row(y, labs, roles):
    xs = [2, 29, 55]; ws = [20, 20, 31]
    for x, w, lab, role in zip(xs, ws, labs, roles):
        box(ax, x, y, w, 10, role, label=lab)
    text(ax, 25.5, y + 5, r'$\times$', 'encre', 'l')
    text(ax, 51.5, y + 5, '=', 'encre', 'l')
text(ax, 44, 70, r'dans $\mathbb{Z}[x]$', 'fixe', 's')
row(56, [r'$2x+3$', r'$3x+5$', r'$6x^2+19x+15$'], ['sujet', 'autre', 'fixe'])
for cx in (12, 39, 70):
    arrow(ax, (cx, 55), (cx, 42), 'varie')
text(ax, 25.5, 48.5, 'modulo 2', 'varie', 's')
row(30, [r'$1$', r'$x+1$', r'$x+1$'], ['sujet', 'autre', 'resultat'])
text(ax, 44, 17, r'$x+1\neq 0$ : $2$ ne divise pas tout $fg$', 'resultat', 's')
text(ax, 44, 10, r'$\overline{D}[x]$ intègre : produit nul impossible', 'fixe', 's')
save(fig, '56-147')
