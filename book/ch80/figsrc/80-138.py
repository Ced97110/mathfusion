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

fig, ax = canvas(70)
box(ax, 2, 56, 38, 10, 'limite', label='complément pas unique', size='s'); box(ax, 48, 56, 38, 10, 'limite', label='distributivité fausse', size='s')
plane(ax, 28, 16, 32, 32, [((30, 32), (58, 32), 'sujet'), ((44, 18), (44, 46), 'varie'), ((32, 20), (56, 44), 'autre')])
arrow(ax, (21, 55.5), (33, 48.8), 'limite'); arrow(ax, (67, 55.5), (55, 48.8), 'limite')
text(ax, 55, 29.5, 'a', 'sujet', 'm', weight='bold'); text(ax, 47, 43.5, r"$a'$", 'varie', 'm', weight='bold'); text(ax, 58.5, 41, r'$a_1$', 'autre', 'm', weight='bold')
text(ax, 14, 32, 'unicité :\nla 2e égalité\néchoue', 'limite', 's'); text(ax, 74, 32, 'distribuer :\nla même\négalité', 'limite', 's')
box(ax, 2, 2, 84, 9, 'fixe', label=r"même défaut : les trois droites $a$, $a'$, $a_1$", size='s')
save(fig, '80-138')
