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

fig, ax = canvas(84)
box(ax, 2, 72, 84, 10, 'sujet', label=r'$B$ muni de $\vee$ et $\wedge$', weight='bold')
for i, s in enumerate(['A1 : commutativité', 'A2 : associativité', 'A3 : distributivité', 'A4 : neutres O et I', 'A5 : compléments']):
    box(ax, 2, 58 - i * 11, 52, 9, 'sujet', label=s, size='s')
arrow(ax, (54.5, 38), (61.5, 38), 'fixe')
box(ax, 62, 26, 24, 24, 'fixe', dash=True, label='se déduisent :\nidempotence\nabsorption', size='s')
text(ax, 44, 8, 'cinq axiomes, sans ordre au départ', 'sujet', 's')
save(fig, '80-140')
