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

fig, ax = canvas(54)
box(ax, 2, 40, 38, 9, 'sujet', label=r'$2\times(3+4)$')
text(ax, 44, 44.5, '=', 'encre', 'l')
box(ax, 48, 40, 38, 9, 'sujet', label=r'$2\times3+2\times4$')
box(ax, 2, 26, 38, 8, 'resultat', label=r'$2\times7=14$')
box(ax, 48, 26, 38, 8, 'resultat', label=r'$6+8=14$')
arrow(ax, (21, 39.5), (21, 34.5), 'fixe'); arrow(ax, (67, 39.5), (67, 34.5), 'fixe')
text(ax, 22, 20.5, r'$\wedge$ comme $\times$', 'varie', 's')
text(ax, 66, 20.5, r'$\vee$ comme $+$', 'varie', 's')
box(ax, 2, 5, 38, 9, 'autre', label=r'$a\wedge(b\vee c)$')
text(ax, 44, 9.5, '=', 'encre', 'l')
box(ax, 48, 5, 38, 9, 'autre', label=r'$(a\wedge b)\vee(a\wedge c)$', size='s')
save(fig, '80-122')
