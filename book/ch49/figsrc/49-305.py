import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def sq(cx, cy, h=10):
    return [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)]
cfg = [(22, 'quart de tour', 1), (66, 'trois quarts de tour', 3)]
for cx, name, k in cfg:
    P = sq(cx, 46)
    poly(ax, P, 'fixe')
    for i, p in enumerate(P):
        disc(ax, p[0], p[1], 3.4, 'varie' if i == 0 else ('resultat' if i == k else 'sujet'), label=str(i + 1), size='s')
    a, b = P[0], P[k]
    arrow(ax, (a[0] + 0.5 * (b[0] - a[0]) * 0 + (b[0] - a[0]) * 0.28, a[1] + (b[1] - a[1]) * 0.28), (b[0] - (b[0] - a[0]) * 0.28, b[1] - (b[1] - a[1]) * 0.28), 'varie', lw=1.3, curve=0.0) if False else arrow(ax, (a[0] + (b[0]-a[0]) * 0.22, a[1] + (b[1]-a[1]) * 0.22), (b[0] - (b[0]-a[0]) * 0.22, b[1] - (b[1]-a[1]) * 0.22), 'varie', lw=1.3)
    text(ax, cx, 27, name, 'encre', 's')
    text(ax, cx, 20, '1 va en %d' % (k + 1), 'resultat', 's')
text(ax, 44, 20, r'$\neq$', 'resultat', 'l') if False else None
box(ax, 8, 3, 72, 11, 'resultat', label='endroits différents : éléments différents', size='s')
save(fig, '49-305')
