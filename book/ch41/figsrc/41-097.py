import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fr = lambda x: f'{x:g}'.replace('.', ',')
u = (1, 3)

def proj(u, v):
    k = (u[0] * v[0] + u[1] * v[1]) / (v[0] ** 2 + v[1] ** 2)
    return k, (k * v[0], k * v[1])

fig, ax = canvas(62)
text(ax, 44, 55, r'$\mathrm{proj}_v\,u=\frac{u\cdot v}{\|v\|^2}\,v$', 'encre', 'l')

def panel(o, s, v, vlabel, vpos, plabel_pos):
    P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
    k, p = proj(u, v)
    arrow(ax, P((0, 0)), P(u), 'sujet')
    arrow(ax, P((0, 0)), P(v), 'autre', lw=2.2 if v == (1, 0) else 1.0)
    arrow(ax, P((0, 0)), P(p), 'resultat', lw=1.0 if v == (1, 0) else 1.6)
    line(ax, [P(u), P(p)], 'fixe', dash=True)
    text(ax, P(u)[0] - 2, P(u)[1] + 1.5, r'$u$', 'sujet')
    text(ax, vpos[0], vpos[1], vlabel, 'autre', 's', ha='left')
    text(ax, plabel_pos[0], plabel_pos[1], f'proj = $\\langle {fr(p[0])}, {fr(p[1])}\\rangle$', 'resultat', 's')
    text(ax, o[0] + 14, 44, f'coefficient {fr(k)}', 'varie', 'm')

panel((5, 10), 7, (4, 2), r'$v=\langle 4, 2\rangle$', (34, 25), (21, 6))
panel((52, 10), 7, (1, 0), r'$v=i$', (62, 10), (62, 5))
save(fig, '41-097')
