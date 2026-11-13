import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax, x, y, r="fixe", s=1.3):
    line(ax, [(x - s, y), (x + s, y)], r, 1.0); line(ax, [(x, y - s), (x, y + s)], r, 1.0)

def equals(ax, x, y, r="fixe", s=1.3):
    line(ax, [(x - s, y + .6), (x + s, y + .6)], r, 1.0); line(ax, [(x - s, y - .6), (x + s, y - .6)], r, 1.0)

def cross(ax, x, y, r="fixe", s=1.0):
    line(ax, [(x - s, y - s), (x + s, y + s)], r, 1.0); line(ax, [(x - s, y + s), (x + s, y - s)], r, 1.0)

def grid(ax, x0, y0, cs, n, role="fixe"):
    for r in range(n):
        for c in range(n):
            box(ax, x0 + c * cs, y0 + (n - 1 - r) * cs, cs, cs, role, r=0.4, lw=0.6)

fig, ax = canvas(64)
cx, cy, R, rr = 30, 33, 22, 5.5
pos = {0: (cx, cy + R), 1: (cx + R, cy), 2: (cx, cy - R), 3: (cx - R, cy)}
for h, (x, y) in pos.items():
    disc(ax, x, y, rr, 'sujet' if h == 2 else 'fixe', label=str(h))
def edge(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d)
p, q = pos[2], pos[1]
arrow(ax, edge(p, q, rr + .8), edge(q, p, rr + .8), 'varie', curve=0.3)
arrow(ax, edge(q, p, rr + .8), edge(p, q, rr + .8), 'resultat', curve=0.3)
text(ax, 14, 5, 'départ', 'sujet', 's')
text(ax, 72, 52, 'ajouter 3', 'varie', 'm'); text(ax, 72, 46, 'de 2 vers 1', 'varie', 's')
text(ax, 72, 30, 'ajouter 1', 'resultat', 'm'); text(ax, 72, 24, 'de 1 vers 2 : retour', 'resultat', 's')
text(ax, 71, 10, r"1 est l'opposé de 3", 'encre', 's')
save(fig, '51-030')
