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

fig, ax = canvas(66)
text(ax, 10, 61, 'a   b', 'encre', 's'); text(ax, 29, 61, 'et', 'sujet', 's'); text(ax, 46, 61, 'ou', 'autre', 's')
for v, (k, role) in zip(['0 0\n0 1\n1 0\n1 1', '0\n0\n0\n1', '0\n1\n1\n1'], [(10, 'encre'), (29, 'sujet'), (46, 'autre')]):
    t = text(ax, k, 42, v, role, 'm'); t.set_linespacing(2.0)
text(ax, 72, 61, 'non', 'varie', 's')
disc(ax, 63, 46, 5, 'sujet', label='0'); disc(ax, 81, 46, 5, 'autre', label='1')
arrow(ax, (64, 51.5), (80, 51.5), 'varie', curve=-0.5); arrow(ax, (80, 40.5), (64, 40.5), 'varie', curve=-0.5)
text(ax, 44, 22, 'parties d’un ensemble $S$ à un seul élément', 'encre', 's')
box(ax, 2, 4, 40, 12, 'sujet', label='0 = ∅ : la partie vide', size='s'); box(ax, 46, 4, 40, 12, 'autre', label='1 = $S$ : l’ensemble', size='s')
save(fig, '80-126')
