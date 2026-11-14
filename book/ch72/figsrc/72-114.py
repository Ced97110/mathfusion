import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, a, b, c, d, res, t):
    text(ax, 2, y + 15, t, 'fixe', 's', ha='left')
    box(ax, 2, y, 11, 10, 'fixe', label=a); box(ax, 14, y, 11, 10, 'sujet', label=b)
    text(ax, 29, y + 5, r'$\sim$' if t == 'espaces' else '=', 'encre', 'l')
    box(ax, 33, y, 11, 10, 'fixe', label=c); box(ax, 45, y, 11, 10, 'autre', label=d)
    arrow(ax, (58, y + 5), (66, y + 5), 'varie'); text(ax, 62, y + 10, 'retirer', 'varie', 's')
    box(ax, 67, y, 19, 10, 'resultat', label=res)
row(36, '3', 'a', '3', 'b', r'$a=b$', 'nombres')
row(10, r'$U_1$', r'$X_1$', r'$U_2$', r'$X_2$', r'$X_1\sim X_2$', 'espaces')
text(ax, 44, 4, r'$U_1\sim U_2$ : même pièce', 'fixe', 's')
save(fig, '72-114')
