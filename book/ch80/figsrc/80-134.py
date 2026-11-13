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

fig, ax = canvas(50)
box(ax, 2, 20, 22, 9, 'sujet', label='{1}'); box(ax, 32, 20, 24, 9, 'varie', label='{2, 3}'); box(ax, 64, 20, 22, 9, 'resultat', label='{1}')
arrow(ax, (24.5, 24.5), (31.5, 24.5), 'varie'); arrow(ax, (56.5, 24.5), (63.5, 24.5), 'varie')
text(ax, 28, 28.5, 'non', 'varie', 's'); text(ax, 60, 28.5, 'non', 'varie', 's')
text(ax, 13, 14, 'a', 'sujet', 'm'); text(ax, 44, 14, r"$a'$", 'varie', 'm'); text(ax, 75, 14, r"$a''=a$", 'resultat', 'm')
arrow(ax, (75, 30), (13, 30), 'fixe', curve=0.3)
text(ax, 44, 44, 'on retrouve la partie de départ', 'fixe', 's')
save(fig, '80-134')
