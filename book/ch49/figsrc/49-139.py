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
text(ax, 60, 101, r'on teste : $gx=x$ ?', 'encre', 'm')
sqr(ax, 17, 61, 9, (1, 3), role='sujet', off='fixe'); text(ax, 17, 46, r'$x$', 'sujet', 'l')
gl = ['1', r'$r$', r'$r^2$', r'$r^3$']; sets = [(1, 3), (2, 4), (1, 3), (2, 4)]
for i in range(4):
    y = 84 - i * 18; same = sets[i] == (1, 3)
    box(ax, 34, y - 8, 52, 16, 'resultat' if same else 'limite')
    text(ax, 42, y, gl[i], 'varie', 'm')
    arrow(ax, (47, y), (55, y), 'varie')
    sqr(ax, 64, y, 5, sets[i], role='fixe', off='fixe', r=1.6)
    text(ax, 78, y, r'$=x$' if same else r'$\neq x$', 'resultat' if same else 'limite', 'm')
text(ax, 44, 14, r'Stab $x$ = {1, $r^2$}', 'resultat', 'l')
save(fig, '49-139')
