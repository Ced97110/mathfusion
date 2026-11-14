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

fig, ax = canvas(66)
text(ax, 22, 61, 'une seule orbite', 'sujet', 'm'); text(ax, 66, 61, 'plusieurs orbites', 'autre', 'm')
box(ax, 3, 8, 38, 47, 'sujet', fill=False)
Q = {1: (14, 42), 2: (30, 42), 3: (30, 22), 4: (14, 22)}
for b in (2, 3, 4): seg(ax, Q[1], Q[b], 4.6, 4.6, 'varie')
for k, (px, py) in Q.items(): disc(ax, px, py, 4, 'sujet' if k == 1 else 'resultat', label=str(k), size='m')
text(ax, 22, 12, 'les 4 sommets', 'sujet', 's')
box(ax, 45, 8, 41, 47, 'autre', fill=False)
sizes = [1, 4, 4, 2, 4, 1]
for idx, n in enumerate(sizes):
    bx = 48 + (idx % 3) * 12.6; by = 34 if idx < 3 else 17
    box(ax, bx, by, 11.4, 11.4, 'autre')
    for t in range(n): disc(ax, bx + 3.4 + (t % 2) * 4.6, by + 3.4 + (t // 2) * 4.6, 1.2, 'autre')
text(ax, 65.5, 12, 'les 16 colorations', 'autre', 's')
save(fig, '49-137')
