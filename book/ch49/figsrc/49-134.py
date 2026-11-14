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

fig, ax = canvas(56)
for k, x in enumerate((15, 35, 55, 75), 1):
    disc(ax, x, 26, 4, 'limite' if k == 2 else 'fixe', label=str(k), size='m')
box(ax, 8, 16, 34, 22, 'sujet', fill=False, dash=True)
box(ax, 28, 12, 34, 22, 'autre', fill=False, dash=True)
text(ax, 25, 43, '1 atteint 1 et 2', 'sujet', 's')
text(ax, 45, 7, '2 atteint 2 et 3', 'autre', 's')
text(ax, 64, 50, '2 est dans deux paquets', 'limite', 's')
arrow(ax, (50, 47.5), (37, 30.5), 'limite')
save(fig, '49-134')
