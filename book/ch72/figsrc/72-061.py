import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 13
def panel(cx, cy, title, e1, e2, d, role, l1, l2):
    P = lambda x, y: (cx + x * s, cy + y * s)
    line(ax, [P(-1.35, 0), P(1.35, 0)], 'fixe', lw=0.6); line(ax, [P(0, -1.35), P(0, 1.35)], 'fixe', lw=0.6)
    arrow(ax, P(0, 0), P(*e1), 'sujet', lw=1.6); arrow(ax, P(0, 0), P(*e2), 'autre', lw=1.6)
    arrow(ax, P(e1[0] * 0.6, e1[1] * 0.6), P(e2[0] * 0.6, e2[1] * 0.6), role, lw=1.1, curve=0.5 if d == 1 else -0.5)
    text(ax, cx, 60, title, 'encre', 's')
    text(ax, cx, 5, d, role, 'l')
    text(ax, *l1[0], l1[1], 'sujet', 's', ha=l1[2]); text(ax, *l2[0], l2[1], 'autre', 's', ha=l2[2])
    return P
P1 = lambda x, y: (22 + x * s, 33 + y * s)
panel(22, 33, 'quart de tour', (0, 1), (-1, 0), r'$\det=1$', 'resultat',
      ((22 + 2, 33 + 1.0 * s + 3), r'$\eta e_1$', 'left'), ((22 - s - 2, 33 + 4), r'$\eta e_2$', 'right'))
panel(66, 33, 'pli horizontal', (1, 0), (0, -1), r'$\det=-1$', 'limite',
      ((66 + s + 1, 33 + 3), r'$\eta e_1$', 'left'), ((66 + 2, 33 - s - 3), r'$\eta e_2$', 'left'))
save(fig, '72-061')
