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

fig, ax = canvas(76)
ys = [8, 27, 46, 65]
N = {'e': (44, ys[0], '∅', 'sujet'), 'a': (18, ys[1], '{1}', 'sujet'), 'b': (44, ys[1], '{2}', 'sujet'), 'c': (70, ys[1], '{3}', 'sujet'),
     'ab': (18, ys[2], '{1, 2}', 'sujet'), 'ac': (44, ys[2], '{1, 3}', 'sujet'), 'bc': (70, ys[2], '{2, 3}', 'sujet'), 'S': (44, ys[3], '{1, 2, 3}', 'sujet')}
E = [('e', 'a'), ('e', 'b'), ('e', 'c'), ('a', 'ab'), ('a', 'ac'), ('b', 'ab'), ('b', 'bc'), ('c', 'ac'), ('c', 'bc'), ('ab', 'S'), ('ac', 'S'), ('bc', 'S')]
hasse(ax, N, E, 22, 8)
text(ax, 2, 8, 'plus petite', 'fixe', 's', ha='left'); text(ax, 2, 65, 'plus grande', 'fixe', 's', ha='left')
text(ax, 86, 8, r'$2\times2\times2$ = 8 parties', 'encre', 's', ha='right')
save(fig, '80-124')
