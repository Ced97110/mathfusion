import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, 'p − 1 : puissance de 2 ?', 'encre', 'm')
rows = [(44, 2, 'resultat', '3 = 2 + 1 : de Fermat'),
        (28, 4, 'resultat', '5 = 4 + 1 : de Fermat'),
        (12, 6, 'limite', '7 = 6 + 1 : pas de Fermat')]
for yb, k, r, t in rows:
    for i in range(k):
        x = 4 + 6 * i
        poly(ax, [(x, yb), (x + 5.6, yb), (x + 5.6, yb + 6), (x, yb + 6)], r)
    x = 4 + 6 * k
    poly(ax, [(x, yb), (x + 5.6, yb), (x + 5.6, yb + 6), (x, yb + 6)], 'fixe')
    brace(ax, 4, 4 + 6 * k - 0.4, yb - 1, r, label=str(k))
    text(ax, 52, yb + 3, t, r, 's', ha='left')
save(fig, '66-107')
