import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fr = lambda x: f'{x:g}'.replace('.', ',')
v = (4, 2)
nv2 = v[0] ** 2 + v[1] ** 2
s = 4.5
fig, ax = canvas(52)

def panel(o, u, hdr_x, label_u, label_p):
    P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
    d = u[0] * v[0] + u[1] * v[1]
    k = d / nv2
    p = (k * v[0], k * v[1])
    arrow(ax, P((0, 0)), P(u), 'sujet', lw=2.0 if k == -1 else 1.0)
    arrow(ax, P((0, 0)), P(v), 'autre')
    arrow(ax, P((0, 0)), P(p), 'resultat', lw=1.0 if k == -1 else 1.6)
    if k != -1:
        line(ax, [P(u), P(p)], 'fixe', dash=True)
    text(ax, hdr_x, 46, f'coefficient ${d}/{nv2}={fr(k)}$' if k != -1 else f'coefficient ${d}/{nv2}={fr(k)}$'.replace('-', '−'), 'varie', 's')
    return P, k, p

Pa, ka, pa = panel((6, 8), (1, 3), 24, 'u', 'p')
text(ax, Pa((1, 3))[0] - 2, Pa((1, 3))[1] + 1.5, r'$u$', 'sujet')
text(ax, Pa(v)[0] + 2, Pa(v)[1] + 1.5, r'$v$', 'autre')
text(ax, Pa(pa)[0] + 3, Pa(pa)[1] - 4.5, f'{fr(ka)} $v$', 'resultat', 's')

Pb, kb, pb = panel((66, 24), (-4, -2), 64, 'u', 'p')
text(ax, Pb(v)[0] - 1, Pb(v)[1] + 3.5, r'$v$', 'autre')
text(ax, Pb(pb)[0] + 2, Pb(pb)[1] - 4.5, r'$u=-1\,v$', 'resultat', 's')
save(fig, '41-099')
