import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
X = [26, 48, 70]
rows = [(52, 'fixe', 'diviseur $d$', ['1', '2', '4']),
        (39, 'sujet', r"$x^{4/d}-1$", [r"$x^4-1$", r"$x^2-1$", r"$x-1$"]),
        (26, 'varie', r"$\mu(d)$", ['1', r"$-1$", '0'])]
for y, role, lab, vals in rows:
    text(ax, 13, y + 4.5, lab, 'fixe', 's')
    for x, v in zip(X, vals):
        box(ax, x, y, 16, 9, role, label=v, size='m')
for x in X: arrow(ax, (x + 8, 26), (x + 8, 21), 'varie')
box(ax, 2, 4, 84, 16, 'resultat', label=r"$\dfrac{x^4-1}{x^2-1}=x^2+1$", size='m')
save(fig, '80-411')
