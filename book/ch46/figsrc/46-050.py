import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pos(h, cx, cy, R):
    a = math.radians(90 - 30 * h); return (cx + R * math.cos(a), cy + R * math.sin(a))

def edge(p, q, off):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * off, p[1] + u[1] * off), (q[0] - u[0] * off, q[1] - u[1] * off)

def clock(ax, cx, cy, R, roles, r=3.0, all_labels=False):
    for h in range(12):
        x, y = pos(h, cx, cy, R)
        if h in roles: disc(ax, x, y, r, roles[h], label=str(h), size="s")
        elif all_labels: disc(ax, x, y, r, "fixe", label=str(h), size="s")
        else: disc(ax, x, y, 0.9, "fixe")

def flow(ax, x, w, items):
    ys = [44, 26, 8]
    for (role, s), y in zip(items, ys):
        box(ax, x, y, w, 11, role, label=s, size="s")
    for y in (44, 26): arrow(ax, (x + w / 2, y), (x + w / 2, y - 7), "fixe")

fig, ax = canvas(72)
cx, cy, R = 21, 31, 14
clock(ax, cx, cy, R, {0: 'varie', 4: 'sujet', 8: 'resultat'})
a, b = edge(pos(0, cx, cy, R), pos(8, cx, cy, R), 3.6); arrow(ax, a, b, 'varie')
text(ax, cx - 2, cy + 1, r'$e-h$', 'varie', 's')
box(ax, 4, 58, 80, 11, 'sujet', label=r'condition : $g,h\in H \Rightarrow g-h\in H$', size='s')
text(ax, cx, 8, 'H = {0, 4, 8}', 'sujet', 's')
flow(ax, 40, 46, [('sujet', 'Départ : e = 0 est dans H'), ('varie', 'Étape : g = e = 0, h = 4'), ('resultat', 'e − h = h⁻¹ = 8, dans H')])
save(fig, '46-050')
