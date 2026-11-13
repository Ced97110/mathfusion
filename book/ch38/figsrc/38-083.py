import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(84)
L = 56.0                      # longueur dessinée de la base (100 %)
x0 = 28
text(ax, 44, 78, 'même erreur de 3° : le point de rencontre glisse', 'encre', 'm')
# référence : la base
ax.add_patch(Rectangle((x0, 60), L, 4, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=2))
text(ax, 4, 62, 'base AB', 'fixe', 's', ha='left')
text(ax, x0 + L / 2, 56, '100 % de la base', 'fixe', 's')
rows = [(36, 60, 6, 'resultat', 'visées à 60°'), (10, 6, 67, 'autre', 'visées à 6°')]
for y, ang, pct, role, lab in rows:
    # les deux visées, tracées avec leur angle exact
    o = (6, y + 6)
    for a in (0, ang):
        line(ax, [o, (o[0] + 15 * math.cos(math.radians(a)), o[1] + 15 * math.sin(math.radians(a)))], role, lw=1.1)
    text(ax, 14, y - 2.2, lab, role, 's')
    w = L * pct / 100
    ax.add_patch(Rectangle((x0, y + 4), w, 4, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, x0 + w + 2, y + 6, f'{pct} % de la base', role, 's', ha='left')
save(fig, '38-083')
