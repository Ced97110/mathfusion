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

fig, ax = canvas(72)
plane(ax, 2, 6, 46, 60, [((5, 36), (45, 36), 'sujet'), ((25, 9), (25, 63), 'varie'), ((10, 21), (40, 51), 'autre')])
text(ax, 35, 32.5, 'axe horizontal', 'sujet', 's'); text(ax, 36, 11, 'axe vertical', 'varie', 's')
text(ax, 15, 52, 'oblique (1, 1)', 'autre', 's'); text(ax, 9, 63, 'plan', 'fixe', 's')
text(ax, 69, 66, 'un axe,\ndeux compléments', 'encre', 's')
box(ax, 52, 48, 34, 10, 'resultat', label='complémenté : oui', size='s')
box(ax, 52, 28, 34, 12, 'fixe', label='distributif :\nun seul complément', size='s')
arrow(ax, (69, 28), (69, 22), 'fixe')
box(ax, 52, 10, 34, 12, 'limite', label='ici : deux compléments\ndonc pas distributif', size='s')
save(fig, '80-131')
