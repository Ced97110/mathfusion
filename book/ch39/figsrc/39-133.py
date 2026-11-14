import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u, cy = 1.8, 36
def panel(cx, z, rz, role_roots, zlabel, labels, vertical):
    arrow(ax, (cx + (-19 if z < 0 else -17), cy), (cx + (19 if z < 0 else 20), cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - 18), (cx, cy + 18), 'fixe', lw=0.6)
    zx = cx + z * u
    disc(ax, zx, cy, 1.5, 'sujet')
    text(ax, zx, cy + 4.5, zlabel, 'sujet', 's')
    r1 = (cx, cy + 3 * u) if vertical else (cx + 3 * u, cy)
    r2 = (cx, cy - 3 * u) if vertical else (cx - 3 * u, cy)
    line(ax, [r1, r2], 'resultat', dash=True, lw=0.8)
    disc(ax, *r1, 1.5, 'resultat'); disc(ax, *r2, 1.5, 'resultat')
    return r1, r2
r1, r2 = panel(19, 9, 3, 'resultat', '9', None, False)
text(ax, r1[0] + 1, cy - 4.5, r'$3$', 'resultat', 's')
text(ax, r2[0] - 1, cy - 4.5, r'$-3$', 'resultat', 's')
r1, r2 = panel(67, -9, 3, 'resultat', r'$-9$', None, True)
text(ax, r1[0] + 5, r1[1], r'$3i$', 'resultat', 's')
text(ax, r2[0] + 5, r2[1], r'$-3i$', 'resultat', 's')
text(ax, 20, 59, r'racines carrées de $9$', 'sujet', 's')
text(ax, 67, 59, r'racines carrées de $-9$', 'sujet', 's')
text(ax, 44, 8, r'$w$ et $-w$ : toujours opposées', 'resultat', 's')
save(fig, '39-133')
