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
box(ax, 4, 20, 30, 24, 'sujet')
text(ax, 19, 37, r'$G$', 'sujet', 'xl'); text(ax, 19, 28, 'des matrices', 'sujet', 's')
box(ax, 54, 8, 30, 38, 'fixe')
for i in range(3):
    for j in range(4):
        disc(ax, 62 + i * 7, 14 + j * 8, 1.3, 'autre')
text(ax, 69, 54, r'$S$ : points du plan', 'autre', 'm')
arrow(ax, (35, 32), (53, 32), 'varie'); text(ax, 44, 36, 'agit', 'varie', 's')
text(ax, 19, 13, 'aucun point dans $G$', 'limite', 's')
save(fig, '49-128')
