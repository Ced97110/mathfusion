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
sqr(ax, 14, 36, 8, (1, 3), role='sujet', off='fixe'); text(ax, 14, 22, r'$x$', 'sujet', 'l')
box(ax, 28, 8, 58, 50, 'sujet', fill=False)
text(ax, 38, 53, r'Stab $x$', 'sujet', 'm')
disc(ax, 47, 28, 5, 'resultat', label='1', size='m'); disc(ax, 71, 28, 5, 'resultat', label=r'$r^2$', size='m')
arrow(ax, (68, 34), (50, 34), 'varie', curve=-0.7); text(ax, 59, 46, 'produit', 'varie', 's')
arrow(ax, (75, 22.5), (68, 22.5), 'varie', curve=-1.6); text(ax, 71, 12, 'inverse', 'varie', 's')
text(ax, 47, 13, 'neutre', 'resultat', 's')
save(fig, '49-141')
