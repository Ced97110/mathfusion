import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [30, 52, 74]
rows = [(38, r'$\sigma \circ \tau$', ['1', '1', '2'], [(r'$\tau$', 'autre'), (r'$\sigma$', 'sujet')]),
        (14, r'$\tau \circ \sigma$', ['1', '2', '3'], [(r'$\sigma$', 'sujet'), (r'$\tau$', 'autre')])]
for y, name, vals, ops in rows:
    text(ax, 12, y, name, 'encre', 'l')
    for i, x in enumerate(xs):
        disc(ax, x, y, 3.6, 'resultat' if i == 2 else 'fixe', label=vals[i], size='m')
    for i in range(2):
        arrow(ax, (xs[i] + 4.2, y), (xs[i + 1] - 4.2, y), ops[i][1])
        text(ax, (xs[i] + xs[i + 1]) / 2, y + 4.5, ops[i][0], ops[i][1], 'm')
text(ax, 74, 26, r'$\neq$', 'limite', 'xl')
save(fig, '42-311')
