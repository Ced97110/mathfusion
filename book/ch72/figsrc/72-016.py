import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(64)
u = 11
def panel(ox, oy):
    axes(ax, ox, oy, u, -0.5, 2.4, -0.5, 1.9)
    return lambda x, y: (ox + x * u, oy + y * u)
P = panel(12, 32)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.4)
text(ax, P(2, 1)[0] + 1, P(2, 1)[1] + 4, '(2, 1)', 'sujet', 's')
text(ax, 22, 12, r'$B(x,x)$ = 5', 'sujet', 'm')
text(ax, 22, 5, r'$\div$ 5 : possible', 'resultat', 's')
Q = panel(56, 32)
disc(ax, *Q(0, 0), 2.0, 'limite')
text(ax, Q(0, 0)[0] + 12, Q(0, 0)[1] + 8, '(0, 0)', 'limite', 's')
text(ax, 66, 12, r'$B(x,x)$ = 0', 'limite', 'm')
text(ax, 66, 5, r'$\div$ 0 : impossible', 'limite', 's')
text(ax, 44, 57, r'il faut $B(x,x)\neq0$', 'encre', 'm')
save(fig, '72-016')
