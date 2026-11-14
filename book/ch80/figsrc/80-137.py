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

fig, ax = canvas(82)
text(ax, 44, 77, r"$a_1$ et $a'$ : deux compléments de $a$", 'encre', 'm')
text(ax, 44, 70.5, r"on veut montrer $a_1=a'$", 'encre', 's')
d = -8
box(ax, 2, 64+d, 84, 10, 'sujet', label=r"$a_1=a_1\wedge(a\vee a')$")
arrow(ax, (14, 63.5+d), (14, 58.5+d), 'fixe'); text(ax, 18, 61+d, r"car $a\vee a'=1$ et 1 est neutre de $\wedge$", 'fixe', 's', ha='left')
box(ax, 2, 48+d, 84, 10, 'varie', label=r"$=(a_1\wedge a)\vee(a_1\wedge a')$", lw=1.8)
arrow(ax, (14, 47.5+d), (14, 42.5+d), 'fixe'); text(ax, 18, 45+d, r"car $a_1\wedge a=0$ et 0 est neutre de $\vee$", 'fixe', 's', ha='left')
text(ax, 84, 53+d, 'on distribue', 'varie', 's', ha='right', weight='bold')
box(ax, 2, 32+d, 84, 10, 'sujet', label=r"$=a_1\wedge a'$")
arrow(ax, (14, 31.5+d), (14, 26.5+d), 'fixe'); text(ax, 18, 29+d, 'donc $a_1\\leq a\'$ ; en échangeant, $a\'\\leq a_1$', 'fixe', 's', ha='left')
box(ax, 2, 16+d, 84, 10, 'resultat', label=r"donc $a_1=a'$ : un seul complément")
save(fig, '80-137')
