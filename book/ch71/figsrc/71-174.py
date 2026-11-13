import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
r2 = math.sqrt(2)
ts = [i / 200 * 2 * math.pi for i in range(201)]
def ell(cx, cy, u, tilted):
    pts = []
    for t in ts:
        s, tt = 0.5 * math.cos(t), math.sin(t)
        pts.append((cx + (s + tt) * u, cy + (s - tt) * u) if tilted else (cx + s * u, cy + tt * u))
    line(ax, pts, 'sujet', lw=1.2)
cl, cr, cy, u = 22, 66, 31, 15
ell(cl, cy, u, True)
arrow(ax, (cl, cy), (cl + 1.2 * u, cy + 1.2 * u), 'varie', lw=1.2)
arrow(ax, (cl, cy), (cl + 1.2 * u, cy - 1.2 * u), 'resultat', lw=1.2)
line(ax, [(cl - 1.1 * u, cy - 1.1 * u), (cl + 1.1 * u, cy + 1.1 * u)], 'varie', dash=True, lw=0.7)
line(ax, [(cl - 1.1 * u, cy + 1.1 * u), (cl + 1.1 * u, cy - 1.1 * u)], 'resultat', dash=True, lw=0.7)
text(ax, cl + 1.2 * u - 1, cy + 1.2 * u + 3, r'$u_1$', 'varie', 's')
text(ax, cl + 1.2 * u - 1, cy - 1.2 * u - 3, r'$u_2$', 'resultat', 's')
ell(cr, cy, 20, False)
arrow(ax, (cr - 18, cy), (cr + 18, cy), 'varie', lw=0.9)
arrow(ax, (cr, cy - 24), (cr, cy + 24), 'resultat', lw=0.9)
text(ax, cr + 18, cy + 3, '$s$', 'varie', 's'); text(ax, cr + 3, cy + 24, '$t$', 'resultat', 's')
text(ax, cl, 60, 'x, y : inclinée', 'sujet', 's'); text(ax, cr, 60, 's, t : droite', 'sujet', 's')
text(ax, 44, 3, 'même courbe, autres coordonnées', 'encre', 's')
save(fig, '71-174')
