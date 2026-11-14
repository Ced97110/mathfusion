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

fig, ax = canvas(58)
text(ax, 22, 54, 'réunion', 'sujet', 'm'); text(ax, 66, 54, 'partie commune', 'sujet', 'm')
for cx, e1, e2, res in [(22, '{1, 2} ∪ {2, 3}', '{2, 3} ∪ {1, 2}', '{1, 2, 3}'), (66, '{1, 2} ∩ {2, 3}', '{2, 3} ∩ {1, 2}', '{2}')]:
    box(ax, cx - 20, 40, 40, 9, 'sujet', label=e1, size='s')
    text(ax, cx, 37.5, '=', 'encre', 'm')
    box(ax, cx - 20, 25, 40, 9, 'autre', label=e2, size='s')
    arrow(ax, (cx, 24.5), (cx, 17.5), 'fixe')
    box(ax, cx - 20, 8, 40, 9, 'resultat', label=res, size='s')
save(fig, '80-141')
