import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
X = lambda x: 44 + 13 * x
Y = lambda v: 50 + 3 * v
xm = 1.5
line(ax, [(X(-1.7), 50), (X(1.7), 50)], 'fixe', lw=0.6)
for s in (-1, 1):
    line(ax, [(X(s * math.pi / 2), 4), (X(s * math.pi / 2), 96)], 'fixe', dash=True)
n = 80; xs = [-xm + i * 2 * xm / n for i in range(n + 1)]
line(ax, [(X(x), Y(math.tan(x))) for x in xs], 'sujet', lw=1.5)
arrow(ax, (X(1.5), Y(14.1)), (X(1.52), 97), 'sujet'); arrow(ax, (X(-1.5), Y(-14.1)), (X(-1.52), 3), 'sujet')
for x, v, lab, ha in ((-1.5, -14.10, '(−1,5 ; −14,10)', 'left'), (0, 0, '(0 ; 0)', 'left'), (1.5, 14.10, '(1,5 ; 14,10)', 'right')):
    disc(ax, X(x), Y(v), 1.5, 'varie')
    text(ax, X(x) + (2.5 if ha == 'left' else -2.5), Y(v) + (0 if v == 0 else (-3 if v < 0 else 3)) + (-3 if v == 0 else 0), lab, 'varie', 's', ha=ha)
text(ax, X(1.5) + 6, 92, '+∞', 'resultat', 'm'); text(ax, X(-1.5) - 6, 8, '−∞', 'resultat', 'm')
text(ax, X(-math.pi / 2) - 0.5, 2, '−π/2', 'fixe', 's'); text(ax, X(math.pi / 2) + 0.5, 2, 'π/2', 'fixe', 's')
save(fig, '30-059')
