import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
v, m, n = (1, 2), 2, 3
assert tuple(m * (n * c) for c in v) == tuple((m * n) * c for c in v) == (6, 12)
assert tuple(c + n + m for c in v) == (6, 7) and tuple(c + m * n for c in v) == (7, 8)
def fmt(a, b): return r'$\langle %s;\ %s\rangle$' % (a, b)
X = [1, 24, 47, 70]
def panel(y, ops, vals, roles, arc_op, verdict, vrole):
    bw, bh = 15, 10
    for i in range(3):
        box(ax, X[i], y, bw, bh, roles[i], label=fmt(*vals[i]), size='s')
    for i in range(2):
        arrow(ax, (X[i] + bw + 0.5, y + bh / 2), (X[i + 1] - 0.5, y + bh / 2), 'fixe', lw=0.9)
        text(ax, (X[i] + bw + X[i + 1]) / 2, y + bh / 2 + 2.6, ops[i], 'fixe', 's')
    box(ax, X[3], y, 17, bh, roles[3], label=fmt(*vals[3]), size='s')
    arrow(ax, (X[0] + bw / 2, y - 0.5), (X[3] + 8.5, y - 0.5), 'fixe', lw=0.9, curve=0.18)
    text(ax, 44, y - 7.5, arc_op, 'fixe', 's')
    text(ax, 44, y - 13.5, verdict, vrole, 's', weight='bold')
panel(58, ['×3', '×2'], [(1, 2), (3, 6), (6, 12), (6, 12)], ['sujet', 'fixe', 'resultat', 'resultat'], '×6 d’un coup', 'deux chemins, même résultat', 'resultat')
panel(20, ['+3', '+2'], [(1, 2), (4, 5), (6, 7), (7, 8)], ['sujet', 'fixe', 'limite', 'limite'], '+6 d’un coup', 'deux chemins, résultats ≠', 'limite')
save(fig, '41-064')
