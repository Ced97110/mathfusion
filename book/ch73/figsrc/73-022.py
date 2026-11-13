import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 12; oy = 14
def panel(ox, cols, vs, role, title, det, tc):
    f = lambda x, y: (ox + u * x, oy + u * y)
    line(ax, [(ox - 1.3 * u, oy), (ox + 2.3 * u, oy)], 'fixe', lw=0.5)
    line(ax, [(ox, oy - 2), (ox, oy + 1.4 * u)], 'fixe', lw=0.5)
    poly(ax, [f(*v) for v in vs], role)
    arrow(ax, f(0, 0), f(*cols[0]), 'varie', lw=1.3)
    arrow(ax, f(0, 0), f(*cols[1]), 'autre', lw=1.3)
    text(ax, tc, 50, title, role, 's')
    text(ax, tc, 43, r'$\det=%s$' % det, role, 'm')
    text(ax, tc, 36.5, 'aire 1', role, 's')
    return f
f = panel(9, [(1, 0), (1, 1)], [(0, 0), (1, 0), (2, 1), (1, 1)], 'resultat', 'cisaillement', '1', 22)
text(ax, f(0.5, 0)[0], oy - 3.4, '(1, 0)', 'varie', 's')
text(ax, f(1, 1)[0] - 4, oy + u + 3, '(1, 1)', 'autre', 's')
g = panel(68, [(-1, 0), (0, 1)], [(0, 0), (-1, 0), (-1, 1), (0, 1)], 'limite', 'réflexion', '−1', 62)
text(ax, g(-0.5, 0)[0], oy - 3.4, '(−1, 0)', 'varie', 's')
text(ax, g(0, 1)[0] + 7, g(0, 1)[1] - 1, '(0, 1)', 'autre', 's')
text(ax, 22, 5.5, 'pas retourné', 'resultat', 's')
text(ax, 62, 5.5, 'retourné', 'limite', 's')
save(fig, '73-022')
