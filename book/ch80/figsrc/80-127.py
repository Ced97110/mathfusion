import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hasse(ax, nodes, edges, bw, bh):
    for a, b in edges:
        (x1, y1, _, _), (x2, y2, _, _) = nodes[a], nodes[b]
        line(ax, [(x1, y1 + bh / 2), (x2, y2 - bh / 2)], 'fixe')
    for k, (cx, cy, lab, role) in nodes.items():
        box(ax, cx - bw / 2, cy - bh / 2, bw, bh, role, label=lab, size='s')
def lens(ax, c1, c2, r, role):
    pts = []
    for k in range(180):
        t = 2 * math.pi * k / 180
        for (a, b) in ((c1, c2), (c2, c1)):
            p = (a[0] + r * math.cos(t), a[1] + r * math.sin(t))
            if math.hypot(p[0] - b[0], p[1] - b[1]) <= r: pts.append(p)
    cx = (c1[0] + c2[0]) / 2; cy = c1[1]
    pts.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    poly(ax, pts, role)
def plane(ax, x, y, w, h, lines):
    box(ax, x, y, w, h, 'fixe')
    for p, q, role in lines: line(ax, [p, q], role, lw=1.6)
    ax.add_patch(Circle((x + w / 2, y + h / 2), 0.9, ec=COL['encre'], fc=COL['encre'], zorder=4))

fig, ax = canvas(56)
text(ax, 44, 50, r'$a\wedge b$', 'sujet', 'xl')
text(ax, 22, 43, 'alarme', 'fixe', 's'); text(ax, 66, 43, 'parties d’un ensemble', 'fixe', 's')
box(ax, 2, 28, 19, 8, 'sujet', label='porte ouverte', size='s'); box(ax, 23, 28, 19, 8, 'autre', label='mode nuit', size='s')
box(ax, 2, 8, 40, 9, 'resultat', label='sonne si les deux', size='s')
arrow(ax, (11.5, 27.5), (15, 17.5), 'fixe'); arrow(ax, (32.5, 27.5), (29, 17.5), 'fixe')
c1 = (59, 26); c2 = (73, 26); r = 12
disc(ax, *c1, r, 'sujet'); disc(ax, *c2, r, 'autre'); lens(ax, c1, c2, r, 'resultat')
text(ax, 52, 26, 'a', 'sujet', 'm'); text(ax, 80, 26, 'b', 'autre', 'm'); text(ax, 66, 26, '∩', 'resultat', 'l')
text(ax, 66, 8, 'a ∩ b : dans les deux', 'resultat', 's')
save(fig, '80-127')
