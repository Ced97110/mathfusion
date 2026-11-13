import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(66)
P = plane(ax, 10, 8, 22, 9.5, (-0.3, 2.4), (-0.2, 5.4))
poly(ax, [P(0, 1), P(2, 1), P(2, 5)], 'sujet'); poly(ax, [P(0, 1), P(1, 1), P(1, 3)], 'fixe')
line(ax, [P(-0.2, 0.6), P(2.2, 5.4)], 'sujet', lw=1.2)
text(ax, 32, 13, 'avancée 2', 'sujet', 's'); text(ax, 57, 46, 'montée 4', 'sujet', 's', ha='left')
box(ax, 64, 8, 22, 10, 'fixe', label=r'petit : $\frac{2}{1}=2$', size='s'); box(ax, 64, 21, 22, 10, 'sujet', label=r'grand : $\frac{4}{2}=2$', size='s')
save(fig, '19-064')
