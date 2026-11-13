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

fig, ax = canvas(92)
box(ax, 4, 76, 80, 12, 'fixe', label=r'départ : $gx=x$ et $hx=x$')
xs = [3, 32, 61]; labs = [r'$1x=x$', r'$(hg)x=x$', r'$g^{-1}x=x$']; tags = ['neutre', 'produit', 'inverse']
for i, x in enumerate(xs):
    role = 'varie' if i == 1 else 'sujet'
    arrow(ax, (x + 12, 75), (x + 12, 60), role)
    box(ax, x, 46, 24, 14, role, label=labs[i], size='s')
    text(ax, x + 12, 42, tags[i], role, 's')
text(ax, 44, 36.5, 'étape clé : 2ᵉ condition', 'varie', 's')
brace(ax, 3, 85, 32, 'fixe')
arrow(ax, (44, 30), (44, 20.5), 'resultat')
box(ax, 14, 8, 60, 12, 'resultat', label=r'Stab $x$ : un sous-groupe')
save(fig, '49-142')
