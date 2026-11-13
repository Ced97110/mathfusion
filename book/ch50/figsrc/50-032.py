import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def row(y, p, chain, q, m):
    text(ax, 3, y + 5, f'p = {p}', 'encre', 's', ha='left')
    xs = [18 + 24 * i for i in range(len(chain))]
    for i, (x, v) in enumerate(zip(xs, chain)):
        box(ax, x, y, 14, 10, 'resultat' if i == len(chain) - 1 else 'sujet', label=str(v), size='l')
        if i < len(chain) - 1:
            arrow(ax, (x + 14.5, y + 5), (xs[i + 1] - 0.5, y + 5), 'varie')
            text(ax, x + 19, y + 12.2, f'÷{p}', 'varie', 's')
    brace(ax, xs[0], xs[-2] + 14, y - 1, 'sujet', label=f'm = {m}')
    text(ax, xs[-1] + 7, y - 5.7, f'q = {q}', 'resultat', 's')
row(40, 2, [12, 6, 3], 3, 2)
row(12, 3, [12, 4], 4, 1)
save(fig, '50-032')
