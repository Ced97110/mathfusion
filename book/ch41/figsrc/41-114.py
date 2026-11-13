import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v = (2, 0), (1, 2)
cr = u[0] * v[1] - u[1] * v[0]
dt = u[0] * v[0] + u[1] * v[1]
nu2, nv2 = u[0] ** 2 + u[1] ** 2, v[0] ** 2 + v[1] ** 2
assert (cr ** 2, dt ** 2, nu2, nv2) == (16, 4, 4, 5) and cr ** 2 + dt ** 2 == nu2 * nv2
fig, ax = canvas(56)
c = 6
x0, y0 = 32, 12
for i in range(nu2):
    for j in range(nv2):
        top = (j == nv2 - 1)
        role = 'autre' if top else 'sujet'
        ax.add_patch(Rectangle((x0 + i * c, y0 + j * c), c, c, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
text(ax, x0 + nu2 * c / 2, y0 + nv2 * c + 4, r'$\|u\|^2=4$', 'encre', 's')
text(ax, x0 - 2, y0 + nv2 * c / 2, r'$\|v\|^2=5$', 'encre', 's', ha='right')
text(ax, x0 + nu2 * c / 2, y0 + 2 * c, '16', 'sujet', 'l')
text(ax, x0 + nu2 * c / 2, y0 + 4.5 * c + 0, '4', 'autre', 'l')
text(ax, x0 + nu2 * c + 2, y0 + 2 * c, r'$\|u\times v\|^2$', 'sujet', 's', ha='left')
text(ax, x0 + nu2 * c + 2, y0 + 4.5 * c, r'$(u\cdot v)^2$', 'autre', 's', ha='left')
text(ax, 44, 5, '16 + 4 = 20 = 4 × 5', 'resultat', 'm')
save(fig, '41-114')
