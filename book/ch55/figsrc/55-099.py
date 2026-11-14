import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
q = 8.0
y0 = 16
cols = [42, 58, 74]
# (rôle, nombre de variables concernées, nombre de copies)
facs = [('sujet', 1, 2), ('autre', 2, 1), ('varie', 3, 1)]
height = [0, 0, 0]
for role, nvar, copies in facs:
    for c in range(nvar):
        for _ in range(copies):
            ax.add_patch(Rectangle((cols[c], y0 + height[c] * q), q, q, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
            height[c] += 1
assert height == [4, 2, 1]
for c in range(3):
    text(ax, cols[c] + q / 2, y0 + height[c] * q + 3, str(height[c]), 'resultat', 'l', weight='bold')
    text(ax, cols[c] + q / 2, y0 - 4, rf'$x_{c + 1}$', 'fixe', 'm')
line(ax, [(38, y0), (86, y0)], 'fixe')
leg = [('sujet', r'$e_1^2\to x_1^2$', 44), ('autre', r'$e_2\to x_1x_2$', 34), ('varie', r'$e_3\to x_1x_2x_3$', 24)]
for role, s, y in leg:
    ax.add_patch(Rectangle((3, y - 2.5), 5, 5, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, 10, y, s, role, 's', ha='left')
text(ax, 62, 66, r'$x_1^4\,x_2^2\,x_3$', 'resultat', 'l', weight='bold')
text(ax, 44, 8, 'un carré = un exposant', 'fixe', 's')
save(fig, '55-099')
