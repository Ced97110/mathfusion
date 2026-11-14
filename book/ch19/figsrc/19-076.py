import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ux, uy = 14, 7
for ox, role, m, up, verb in [(8, 'sujet', r'$m=2$', True, 'monte 2'), (50, 'autre', r'$m=-2$', False, 'descend 2')]:
    P = lambda x, y: (ox + x * ux, 10 + y * uy)
    arrow(ax, (ox, 10), (ox + 2 * ux, 10), 'fixe', lw=0.8); arrow(ax, (ox, 10), (ox, 10 + 4 * uy), 'fixe', lw=0.8)
    a, b = (1, 3) if up else (3, 1)
    if up: line(ax, [P(0, 1), P(1.5, 4)], role, lw=1.4)
    else: line(ax, [P(0, 3), P(1.5, 0)], role, lw=1.4)
    arrow(ax, P(0, a), P(1, a), 'fixe', lw=0.9); arrow(ax, P(1, a), P(1, b), 'varie', lw=1.1)
    text(ax, P(0.5, a)[0], P(0, a)[1] + (-3 if up else 3), 'avance 1', 'fixe', 's')
    text(ax, P(1, 2)[0] + 2.5, P(0, 2)[1], verb, 'varie', 's', ha='left')
    text(ax, ox + 14, 46, m, role, 'l')
text(ax, 44, 3.5, 'lue de gauche à droite', 'fixe', 's')
save(fig, '19-076')
