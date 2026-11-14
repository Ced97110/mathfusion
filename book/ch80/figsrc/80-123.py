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
text(ax, 44, 66, r"$a'$ est le complément de $a$", 'sujet', 's')
box(ax, 14, 50, 28, 9, 'sujet', label=r'$a$ = {1}')
box(ax, 46, 50, 28, 9, 'varie', label=r"$a'$ = {2, 3}")
brace(ax, 16, 72, 49.5, 'fixe')
arrow(ax, (44, 47.5), (21, 40.5), 'fixe'); arrow(ax, (44, 47.5), (67, 40.5), 'fixe')
box(ax, 2, 31, 40, 9, 'resultat', label=r"$a\vee a'$ = {1, 2, 3} = 1", size='s')
box(ax, 46, 31, 40, 9, 'resultat', label=r"$a\wedge a'$ = ∅ = 0", size='s')
text(ax, 44, 22, 'voisins : une opération chacun', 'fixe', 's')
box(ax, 2, 7, 38, 9, 'fixe', label=r'$n+(-n)=0$')
box(ax, 48, 7, 38, 9, 'fixe', label=r'$n\times n^{-1}=1$')
save(fig, '80-123')
