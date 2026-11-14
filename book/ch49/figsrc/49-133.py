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

fig, ax = canvas(106)
box(ax, 2, 2, 84, 48, 'varie')
text(ax, 4, 45, 'transitive : étape clé', 'varie', 'm', ha='left')
text(ax, 4, 100, r'réflexive : $1x=x$', 'sujet', 'm', ha='left')
text(ax, 4, 72, r'symétrique : $x=g^{-1}y$', 'sujet', 'm', ha='left')
disc(ax, 44, 86, 4, 'sujet', label=r'$x$')
arrow(ax, (41, 90), (47, 90), 'varie', curve=-2.2)
disc(ax, 22, 60, 4, 'sujet', label=r'$x$'); disc(ax, 66, 60, 4, 'sujet', label=r'$y$')
arrow(ax, (26.5, 62), (61.5, 62), 'varie', curve=0.0); text(ax, 44, 66, r'$g$', 'varie', 's')
arrow(ax, (61.5, 58), (26.5, 58), 'varie'); text(ax, 44, 54, r'$g^{-1}$', 'varie', 's')
for x, l in ((14, 'x'), (44, 'y'), (74, 'z')): disc(ax, x, 14, 4, 'sujet', label='$%s$' % l)
arrow(ax, (18.5, 14), (39.5, 14), 'varie'); text(ax, 29, 17.5, r'$g$', 'varie', 's')
arrow(ax, (48.5, 14), (69.5, 14), 'varie'); text(ax, 59, 17.5, r'$h$', 'varie', 's')
arrow(ax, (15, 19), (73, 19), 'resultat', curve=-0.3); text(ax, 44, 33, r'$hg$', 'resultat', 'm')
save(fig, '49-133')
