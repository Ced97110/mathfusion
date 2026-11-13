import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
u = 9.0
box(ax, 4, 72, 80, 11, 'resultat', label=r'$M_i$ directs $\Rightarrow$ $M=\oplus M_{ij}$ direct', size='s')
text(ax, 22, 66, 'cela marche', 'resultat', 's', weight='bold')
text(ax, 66, 66, 'cela tombe', 'limite', 's', weight='bold')

def panel(ox, oy, diag):
    P = lambda x, y: (ox + x * u, oy + y * u)
    line(ax, [P(-1.0, 0), P(2.4, 0)], 'sujet', lw=1.4)
    line(ax, [P(0, -0.6), P(0, 2.0)], 'autre', lw=1.4)
    if diag:
        line(ax, [P(-0.5, -0.5), P(2.0, 2.0)], 'varie', lw=1.4)
        arrow(ax, P(0, 0), P(0.93, 0.93), 'varie', lw=1.1)
    arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.1)
    arrow(ax, P(1, 0), P(1, 0.93), 'autre', lw=1.1)
    disc(ax, *P(1, 1), 1.3, 'limite' if diag else 'resultat')
    text(ax, P(1, 1)[0] + 2.5, P(1, 1)[1] - 4.5, '(1, 1)', 'limite' if diag else 'resultat', 's', ha='left')
    return P
panel(14, 40, False)
P = panel(58, 40, True)
text(ax, P(2.0, 2.0)[0] - 1, P(2.0, 2.0)[1] + 3, 'diagonale', 'varie', 's', ha='right')
text(ax, 22, 21, 'horizontal ⊕ vertical :\n(1, 1) = (1, 0) + (0, 1)\nune seule écriture', 'resultat', 's')
text(ax, 66, 21, 'avec la diagonale :\n(1, 1) = (1, 0) + (0, 1)\n(1, 1) = 1·(1, 1)\ndeux écritures', 'limite', 's')
save(fig, '58-277')
