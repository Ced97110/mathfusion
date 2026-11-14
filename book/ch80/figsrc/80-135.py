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

def demorgan(code, ha, hb, hu, rowA, rowB, capA, capB, ra, rb, rc, rd, fin, ops):
    fig, ax = canvas(64)
    text(ax, 44, 59, ha, 'encre', 'm')
    text(ax, 2, 53, capA, 'sujet', 's', ha='left')
    box(ax, 2, 39, 33, 9, 'sujet', label=ra, size='s'); arrow(ax, (36, 43.5), (52.5, 43.5), 'varie'); text(ax, 44.5, 47.5, ops[0], 'varie', 's')
    box(ax, 53, 39, 33, 9, 'resultat', label=rb, size='s')
    text(ax, 69.5, 30, '=', 'encre', 'l')
    text(ax, 2, 24, capB, 'autre', 's', ha='left')
    box(ax, 2, 5, 33, 13, 'autre', label=rc, size='s'); arrow(ax, (36, 11.5), (52.5, 11.5), 'varie'); text(ax, 44.5, 15.5, ops[1], 'varie', 's')
    box(ax, 53, 7, 33, 9, 'resultat', label=rd, size='s')
    save(fig, code)

demorgan('80-135', r'$a$ = {1}      $b$ = {2}      $S$ = {1, 2, 3}', '', '', 0, 0, 'réunir, puis compléter', 'compléter, puis ∩',
 r'$a\vee b$ = {1, 2}', r"$(a\vee b)'$ = {3}", "$a'$ = {2, 3}\n$b'$ = {1, 3}", r"$a'\wedge b'$ = {3}", 0, ('complément', 'en commun'))
