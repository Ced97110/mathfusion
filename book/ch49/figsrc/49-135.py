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

fig, ax = canvas(52)
box(ax, 3, 20, 22, 28, 'sujet'); text(ax, 14, 43, r'$S$', 'sujet', 'l')
for i in range(4):
    for j in range(4): disc(ax, 8 + i * 4, 24.5 + j * 4, 1.1, 'sujet')
text(ax, 28.5, 33, '/', 'encre', 'xl')
box(ax, 31, 20, 16, 28, 'varie'); text(ax, 39, 43, r'$G$', 'varie', 'l')
for i in range(4): disc(ax, 33.5 + i * 4, 30, 1.1, 'varie')
arrow(ax, (49, 34), (59, 34), 'fixe')
box(ax, 61, 20, 25, 28, 'resultat'); text(ax, 73.5, 43, r'$S/G$', 'resultat', 'l')
for i in range(3):
    for j in range(2): disc(ax, 67.5 + i * 6, 28 + j * 5, 1.5, 'resultat')
text(ax, 14, 14, '16 colorations', 'sujet', 's'); text(ax, 39, 14, '4 rotations', 'varie', 's'); text(ax, 73.5, 14, '6 orbites', 'resultat', 's')
save(fig, '49-135')
