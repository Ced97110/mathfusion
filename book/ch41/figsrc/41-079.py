import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
panels = [(3, 'same', r'$\theta=0^\circ$', r'$\cos\theta=1$'),
          (32, 'perp', r'$\theta=90^\circ$', r'$\cos\theta=0$'),
          (61, 'opp', r'$\theta=180^\circ$', r'$\cos\theta=-1$')]
L, M = 17, 11
for x0, kind, head, val in panels:
    ox, oy = x0 + 12, 32
    text(ax, x0 + 12, 52, head, 'encre', 'm')
    if kind == 'same':
        arrow(ax, (ox - 8, oy), (ox - 8 + L, oy), 'sujet', lw=1.6)
        arrow(ax, (ox - 8, oy), (ox - 8 + M, oy), 'autre', lw=1.6)
        text(ax, ox - 8 + L - 3, oy + 3.5, r'$u$', 'sujet', 'm')
        text(ax, ox - 8 + M - 3, oy - 3.5, r'$v$', 'autre', 'm')
    elif kind == 'perp':
        arrow(ax, (ox - 6, oy - 6), (ox - 6 + L, oy - 6), 'sujet', lw=1.6)
        arrow(ax, (ox - 6, oy - 6), (ox - 6, oy - 6 + L), 'autre', lw=1.6)
        line(ax, [(ox - 6 + 3, oy - 6), (ox - 6 + 3, oy - 3), (ox - 6, oy - 3)], 'fixe', lw=0.8)
    else:
        arrow(ax, (ox, oy), (ox + 9, oy), 'sujet', lw=1.6)
        arrow(ax, (ox, oy), (ox - 11, oy), 'autre', lw=1.6)
    box(ax, x0, 8, 24, 9, 'resultat', label=val, size='m')
text(ax, 44, 3, 'toujours entre $-1$ et $1$', 'fixe', 's')
save(fig, '41-079')
