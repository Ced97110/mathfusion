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

fig, ax = canvas(50)
f = numberline(ax, 8, 74, 24, 0, 7, arrow_right=False)
arrow(ax, (f(0), 27), (f(5), 27), 'resultat', curve=-0.35)
text(ax, (f(0) + f(5)) / 2, 37, r'+5', 'resultat', 'm')
arrow(ax, (f(5), 17), (f(0), 17), 'limite', curve=-0.35)
text(ax, (f(0) + f(5)) / 2, 8.5, r'$\times$', 'limite', 'l')
text(ax, 44, 46, '0 atteint 5 en ajoutant 5', 'resultat', 's')
text(ax, 44, 3.5, "5 n'atteint pas 0", 'limite', 's')
save(fig, '49-131')
