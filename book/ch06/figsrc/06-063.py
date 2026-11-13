import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [(42, r'$\frac{3}{4}\div\frac{2}{5}$', r'$\frac{3}{4}$', r'$\frac{5}{2}$', r'$=\frac{15}{8}$'),
        (22, r'$\frac{1}{2}\div\frac{1}{3}$', r'$\frac{1}{2}$', r'$\frac{3}{1}$', r'$=\frac{3}{2}$')]
for y, left, a, b, res in rows:
    text(ax, 17, y, left, 'encre', 'l')
    arrow(ax, (32, y), (40, y), 'varie')
    text(ax, 48, y, a, 'fixe', 'l'); text(ax, 56, y, r'$\times$', 'varie', 'l')
    text(ax, 64, y, b, 'varie', 'l'); text(ax, 78, y, res, 'resultat', 'l')
text(ax, 25, 6, 'gris : ne change pas', 'fixe', 's'); text(ax, 65, 6, 'orange : change', 'varie', 's')
save(fig, '06-063')
