import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

EM = ' '
def pitch(size='m'):
    return 1.636 * SIZE[size] * 25.4 / 72
def rowstr(vals):
    return EM.join(vals)
def brk(ax, cx, cy, hw, hh, role='encre'):
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.3, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.3, cy - hh)], role, lw=0.8)
def mat2(ax, cx, cy, r1, r2, role='encre', size='m'):
    text(ax, cx, cy + 3.2, rowstr(r1), role, size); text(ax, cx, cy - 3.2, rowstr(r2), role, size)
    brk(ax, cx, cy, 4.8, 5.4, role)

fig, ax = canvas(56)
ox, oy, u = 14, 27, 5
arrow(ax, (4, oy), (50, oy), 'fixe'); arrow(ax, (ox, 5), (ox, 52), 'fixe')
zx = ox + 3 * u
line(ax, [(zx, oy + 4 * u), (zx, oy - 4 * u)], 'fixe', dash=True)
disc(ax, zx, oy + 4 * u, 1.4, 'sujet'); disc(ax, zx, oy - 4 * u, 1.4, 'autre'); disc(ax, zx, oy, 1.4, 'resultat')
text(ax, zx + 3, oy + 4 * u, r'$z=3+4i$', 'sujet', 's', ha='left')
text(ax, zx + 3, oy - 4 * u, r'$\bar z=3-4i$', 'autre', 's', ha='left')
text(ax, zx, oy - 4, '3', 'resultat', 's')
text(ax, ox - 4, oy + 4 * u, '4', 'fixe', 's'); text(ax, ox - 4.5, oy - 4 * u, '$-4$', 'fixe', 's')
text(ax, 73, 40, r'$z+\bar z=6$', 'resultat', 'm'); text(ax, 73, 34, r'$=2a$', 'resultat', 'm')
text(ax, 73, 20, r'$z\,\bar z=25$', 'resultat', 'm'); text(ax, 73, 14, r'$=a^2+b^2$', 'resultat', 'm')
save(fig, '77-123')
