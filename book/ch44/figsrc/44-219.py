import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(80)
cw = 8.5; x0, ytop = 24, 66
isrot = lambda k: k in ('1', 's', 'q')
for r, a in enumerate(ORDER):
    for c, b in enumerate(ORDER):
        rot = isrot(comp(a, b))
        box(ax, x0 + c * cw + .3, ytop - (r + 1) * cw + .3, cw - .6, cw - .6, 'sujet' if rot else 'autre', r=0.4, lw=0)
for c0, name, role in [(0, 'rotations', 'sujet'), (3, 'retournements', 'autre')]:
    text(ax, x0 + (c0 + 1.5) * cw, ytop + 4, name, role, 's', weight='bold')
    text(ax, x0 - 4, ytop - (c0 + 1.5) * cw, name, role, 's', weight='bold', rot=90)
for r in (0, 1):
    for c in (0, 1):
        rot = isrot(comp(ORDER[3 * r], ORDER[3 * c]))
        text(ax, x0 + (3 * c + 1.5) * cw, ytop - (3 * r + 1.5) * cw, 'rotation' if rot else 'retournement', 'sujet' if rot else 'autre', 's', weight='bold')
save(fig, '44-219')
