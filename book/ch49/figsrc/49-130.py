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

fig, ax = canvas(62)
xs = [12, 34, 56, 78]; sets = [(1, 3), (2, 4), (1, 3), (2, 4)]
gl = ['1', r'$r$', r'$r^2$', r'$r^3$']; tx = ['sommets 1, 3', 'sommets 2, 4', 'sommets 1, 3', 'sommets 2, 4']
for i, x in enumerate(xs):
    text(ax, x, 55, gl[i], 'varie', 'm')
    arrow(ax, (x, 51.5), (x, 44.5), 'varie')
    sqr(ax, x, 34, 6, sets[i], num=(i == 0), role='sujet' if i % 2 == 0 else 'resultat', off='fixe', r=2.1)
    text(ax, x, 21, tx[i], 'sujet' if i % 2 == 0 else 'resultat', 's')
brace(ax, 4, 84, 15, 'resultat', label=r'$Gx$ : 2 colorations', depth=1.6)
save(fig, '49-130')
