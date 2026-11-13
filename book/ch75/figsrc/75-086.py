import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s = 6.5; oy = 38
def panel(cx, title, k, cap, role):
    P = lambda x, y: (cx + x * s * k, oy + y * s * k)
    line(ax, [(cx - 14, oy), (cx + 14, oy)], 'fixe', lw=0.5); line(ax, [(cx, oy - 12), (cx, oy + 14)], 'fixe', lw=0.5)
    a = (1, 0); b = (0, 1)
    poly(ax, [P(0, 0), P(a[0], 0), P(a[0], b[1]), P(0, b[1])], role)
    arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.0); arrow(ax, P(0, 0), P(0, 1), 'sujet', lw=1.0)
    text(ax, cx, 59, title, 'encre', 'l'); text(ax, cx, 25, cap, role, 's')
panel(15, r'$\times 1$', 1, 'aire 1', 'resultat')
panel(44, r'$\times(-1)$', -1, 'aire 1', 'resultat')
panel(73, r'$\times 2$', 2, 'aire 4 : exclu', 'limite')
text(ax, 44, 67, 'multiplier toutes les flèches par :', 'encre', 'm')
brace(ax, 3, 58, 19, 'resultat', label=r'seuls $c=1$ et $c=-1$ : le centre', size='s')
text(ax, 44, 3, r'ils commutent avec toutes les autres', 'resultat', 's')
save(fig, '75-086')
