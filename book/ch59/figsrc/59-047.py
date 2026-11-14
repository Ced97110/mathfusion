import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 14, 50, 'nombre', 'sujet', 'm'); text(ax, 52, 50, 'son inverse', 'encre', 'm')
rows = [('1', '1', True, 36), ('−1', '−1', True, 23), ('2', r'$\frac{1}{2}$', False, 10)]
for n, inv, ok, y in rows:
    box(ax, 5, y, 18, 10, 'sujet', label=n)
    arrow(ax, (24, y + 5), (39, y + 5), 'varie')
    box(ax, 40, y, 24, 10, 'resultat' if ok else 'limite', label=inv)
    text(ax, 76, y + 5, r'$\in\mathbb{Z}$' if ok else r'$\notin\mathbb{Z}$', 'resultat' if ok else 'limite', 'l')
save(fig, '59-047')
