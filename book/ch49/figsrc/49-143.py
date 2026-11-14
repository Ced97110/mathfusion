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
text(ax, 22, 60, r'$Gx$', 'sujet', 'xl')
text(ax, 62, 60, 'pas un produit', 'limite', 'm')
arrow(ax, (22, 55), (22, 36), 'sujet')
box(ax, 3, 4, 84, 40, 'fixe', fill=False)
text(ax, 44, 40, r'$S$ : 16 colorations', 'fixe', 's')
box(ax, 6, 8, 34, 26, 'sujet')
sqr(ax, 15, 18, 5.5, (1, 3), role='fixe', off='fixe', r=1.7); sqr(ax, 31, 18, 5.5, (2, 4), role='fixe', off='fixe', r=1.7)
text(ax, 23, 30.5, r'$Gx$ : 2 colorations', 'sujet', 's')
for i in range(7):
    for j in range(2): disc(ax, 48 + i * 5, 15 + j * 7, 1.5, 'fixe')
save(fig, '49-143')
