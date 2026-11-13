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

fig, ax = canvas(74)
text(ax, 22, 69, 'avec distributivité', 'resultat', 's'); text(ax, 66, 69, 'sans distributivité', 'limite', 's')
box(ax, 12, 52, 20, 9, 'sujet', label=r'$a$ = {1}', size='s')
box(ax, 6, 34, 32, 9, 'varie', label=r"$a'$ = {2, 3}", size='s')
arrow(ax, (22, 51.5), (22, 43.5), 'varie'); text(ax, 24, 47.5, 'complément', 'varie', 's', ha='left')
box(ax, 2, 10, 40, 9, 'resultat', label='un seul complément', size='s')
plane(ax, 48, 24, 38, 38, [((50, 43), (84, 43), 'sujet'), ((67, 26), (67, 60), 'varie'), ((52, 28), (82, 58), 'autre')])
text(ax, 76, 40, 'horizontal', 'sujet', 's'); text(ax, 75, 28, 'vertical', 'varie', 's'); text(ax, 58, 58, 'diagonale', 'autre', 's')
box(ax, 48, 10, 38, 9, 'limite', label='plusieurs compléments', size='s')
save(fig, '80-133')
