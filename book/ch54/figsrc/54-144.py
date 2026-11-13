import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
w, u = 7, 3
X = lambda p: 46 + 12 * (3 - p)
rows = [(80, 'f : degré 3', {3: 1, 2: -2, 1: 0, 0: 4}, 'sujet'),
        (58, 'reste : degré 2', {2: -1, 1: 0, 0: 4}, 'sujet'),
        (36, 'reste : degré 1', {1: -1, 0: 4}, 'sujet'),
        (14, 'reste 3 : degré 0', {0: 3}, 'resultat')]
steps = [r'terme $x^2$ : retire $x^2(x-1)$', r'terme $-x$ : retire $-x\,(x-1)$', r'terme $-1$ : retire $-1\,(x-1)$']
for k, (yb, lab, co, rl) in enumerate(rows):
    line(ax, [(40, yb), (86, yb)], 'fixe')
    text(ax, 2, yb + 5, lab, rl, 's', ha='left', weight='bold' if rl == 'resultat' else 'normal')
    for p in range(4):
        a = co.get(p, 0)
        if a == 0:
            line(ax, [(X(p) - w / 2, yb), (X(p) + w / 2, yb)], 'fixe', lw=1.2)
        else:
            ax.add_patch(Rectangle((X(p) - w / 2, min(yb, yb + a * u)), w, abs(a * u), ec=COL[rl], fc=FILL[rl], lw=0.8, zorder=2))
for k, st in enumerate(steps):
    ym = rows[k][0] - 11
    text(ax, 2, ym, st, 'varie', 's', ha='left')
for p in range(4):
    text(ax, X(p), 6, f'$x^{p}$' if p > 1 else ('$x$' if p == 1 else '1'), 'fixe', 's')
text(ax, 2, 6, r'quotient $x^2-x-1$', 'resultat', 's', ha='left', weight='bold')
save(fig, '54-144')
