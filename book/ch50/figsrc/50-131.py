import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def clock(cx, cy, order, role, cap):
    R = 13; r = 3.4
    pos = {i: (cx + R * math.cos(math.radians(90 - 72 * i)), cy + R * math.sin(math.radians(90 - 72 * i))) for i in range(5)}
    for a, b in zip(order[:-1], order[1:]):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        arrow(ax, (x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r), role, curve=0.0)
    for i, (px, py) in pos.items():
        disc(ax, px, py, r, 'fixe' if i == 0 else 'sujet', label=str(i), size='m')
    text(ax, cx, cy - 22, cap, role, 's')
text(ax, 44, 79, r'$p=5$ : 5 éléments', 'sujet', 'm')
clock(22, 52, [0, 1, 2, 3, 4, 0], 'varie', 'élément 1 : 5 pas')
clock(66, 52, [0, 2, 4, 1, 3, 0], 'autre', 'élément 2 : 5 pas')
text(ax, 44, 17, 'retour à 0 après 5 pas', 'resultat', 'm')
text(ax, 44, 8, r"tout élément $\neq$ 0 : ordre 5", 'resultat', 's')
save(fig, '50-131')
