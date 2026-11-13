import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def clock(cx, k, title, start, result, eq):
    cy, R = 40, 15
    pts = [(cx + R * math.sin(2 * math.pi * i / k), cy + R * math.cos(2 * math.pi * i / k)) for i in range(k)]
    for i, (x, y) in enumerate(pts):
        steps = [(start + s) % k for s in range(1, 5)]
        role = 'sujet' if i == start else 'resultat' if i == result else 'varie' if i in steps else 'fixe'
        disc(ax, x, y, 1.9 if role == 'fixe' else 2.4, role)
    text(ax, pts[0][0], pts[0][1] + 5.5, '0', 'fixe', 's')
    text(ax, cx, cy + 2, title, 'encre', 'm'); text(ax, cx, cy - 4, 'départ 5', 'sujet', 's')
    text(ax, cx, 8, eq, 'resultat', 'm')
clock(23, 12, 'k = 12', 5, 9, '5 + 4 = 9')
clock(65, 7, 'k = 7', 5, 2, '5 + 4 = 2')
text(ax, 44, 67, '4 pas de 1, le tour recommence', 'varie', 's')
save(fig, '52-079')
