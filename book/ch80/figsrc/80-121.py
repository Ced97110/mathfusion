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

fig, ax = canvas(72)
N = {'v': (22.5, 12, '∅ = 0', 'sujet'), 'a': (10, 32, '{1}', 'sujet'), 'b': (35, 32, '{2}', 'sujet'), 't': (22.5, 52, '{1, 2} = 1', 'sujet')}
box(ax, 0.5, 3, 44, 56, 'sujet', fill=False, dash=True)
hasse(ax, N, [('v', 'a'), ('v', 'b'), ('a', 't'), ('b', 't')], 15, 8)
arrow(ax, (18, 32), (27, 32), 'varie', both=True)
text(ax, 22, 65, 'parties de {1, 2}', 'sujet', 's')
text(ax, 68, 65, 'quatre conditions', 'sujet', 's')
for yc, s, tgt in [(52, 'plus grand : 1', (30.2, 52)), (42, 'treillis : sup et inf', (44.5, 42)), (32, 'complément de {1} : {2}', (42.7, 32)), (22, 'distributif', (44.5, 22)), (12, 'plus petit : 0', (30.2, 12))]:
    box(ax, 50, yc - 4, 36, 8, 'sujet', label=s, size='s')
    arrow(ax, (50, yc), tgt, 'fixe', lw=0.8)
save(fig, '80-121')
