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

fig, ax = canvas(80)
text(ax, 14, 75, 'signe abstrait', 'sujet', 's'); text(ax, 60, 75, 'sur les parties de S', 'autre', 's')
L = ['≤', r'$a\wedge b$', r'$a\vee b$', '0', '1', r"$a'$"]
R = ['⊆ : {1} ⊆ {1, 2}', '∩ : {1} ∩ {1, 2} = {1}', '∪ : {1} ∪ {1, 2} = {1, 2}', '∅ : la partie vide', 'S = {1, 2, 3}', 'reste de S sans a : {2, 3}']
for i in range(6):
    y = 62 - i * 12
    box(ax, 2, y, 24, 9, 'sujet', label=L[i])
    arrow(ax, (26.5, y + 4.5), (33.5, y + 4.5), 'fixe', both=True)
    box(ax, 34, y, 52, 9, 'autre', label=R[i], size='s')
save(fig, '80-125')
