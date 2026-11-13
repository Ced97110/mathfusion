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

fig, ax = canvas(76)
for i, l in enumerate(['1', r'$r$', r'$r^2$', r'$r^3$']): text(ax, 35.5 + i * 13, 68, l, 'varie', 'm')
rows = [((), (0, 1, 2, 3)), ((1, 3), (0, 2)), ((1,), (0,))]
for j, (on, ok) in enumerate(rows):
    y = 54 - j * 18
    sqr(ax, 12, y, 5.5, on, role='fixe', off='sujet', r=1.8)
    for i in range(4):
        good = (i in ok) if j else True
        box(ax, 30 + i * 13, y - 3.5, 11, 7, 'resultat' if i in ok else 'fixe', fill=(i in ok), dash=(i not in ok))
    text(ax, 84, y, str(len(ok)), 'resultat', 'm')
box(ax, 4, 2, 8, 5, 'resultat'); text(ax, 15, 4.5, 'la laisse en place', 'resultat', 's', ha='left')
save(fig, '49-138')
