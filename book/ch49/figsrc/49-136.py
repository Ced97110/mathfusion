import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sqr(ax, cx, cy, h, on=(), num=False, role='fixe', off='sujet', r=None):
    """Carré de centre (cx, cy), demi-côté h ; sommets 1 (haut gauche) à 4 dans le sens horaire ; pions orange sur 'on'."""
    r = r or max(1.6, h * 0.32)
    P = {1: (cx - h, cy + h), 2: (cx + h, cy + h), 3: (cx + h, cy - h), 4: (cx - h, cy - h)}
    poly(ax, [P[k] for k in (1, 2, 3, 4)], role)
    for k, (px, py) in P.items():
        rl = 'varie' if k in on else off
        if num:
            disc(ax, px, py, r, rl, label=str(k), size='s')
        else:
            ax.add_patch(Circle((px, py), r, ec=COL[rl], fc=COL[rl], lw=0.6, zorder=3))

def seg(ax, p, q, ra, rb, role='varie', curve=0.0):
    """Flèche de p à q, raccourcie de ra au départ et rb à l'arrivée."""
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + ux * ra, p[1] + uy * ra), (q[0] - ux * rb, q[1] - uy * rb), role, curve=curve)

fig, ax = canvas(60)
sizes = [1, 4, 4, 2, 4, 1]; sp = 3.2; ws = [n * sp + 2 for n in sizes]; gap = 3
x = (88 - sum(ws) - gap * 5) / 2
text(ax, 44, 55, r'$S$ : 16 colorations rangées en paquets', 'sujet', 's')
for n, w in zip(sizes, ws):
    box(ax, x, 34, w, 9, 'sujet')
    for i in range(n): disc(ax, x + 1 + sp / 2 + i * sp, 38.5, 0.95, 'sujet')
    arrow(ax, (x + w / 2, 33), (x + w / 2, 21.5), 'varie')
    disc(ax, x + w / 2, 17.5, 3.5, 'resultat')
    x += w + gap
text(ax, 44, 6, r'$S/G$ : 6 éléments, un par paquet', 'resultat', 's')
save(fig, '49-136')
