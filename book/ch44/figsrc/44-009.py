import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

POS = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # coin en haut a droite, haut a gauche, bas a gauche, bas a droite
def P(k, refl=False):
    """Position (indice dans POS) des coins 1 a 4 apres s (si refl) puis r^k."""
    return [((3 - i) + k) % 4 if refl else (i + k) % 4 for i in range(4)]
def tile(ax, cx, cy, h, idx, nums='mark', role='sujet'):
    poly(ax, [(cx + h, cy + h), (cx - h, cy + h), (cx - h, cy - h), (cx + h, cy - h)], role)
    r = 0.26 * h
    for i in range(4):
        px, py = POS[idx[i]]; x, y = cx + px * h * 0.62, cy + py * h * 0.62
        if i == 0: disc(ax, x, y, r, 'varie', label=None if nums == 'mark' else '1')
        elif nums == 'all': disc(ax, x, y, r, 'fixe', label=str(i + 1))
        elif nums == 'mark' and i == 1: disc(ax, x, y, r * 0.6, 'fixe')

fig, ax = canvas(66)
def sides(cx, cy, h, idx):
    r = 0.26 * h
    for i in range(4):
        a = POS[idx[i]]; b = POS[idx[(i + 1) % 4]]
        p = (cx + a[0] * h * 0.62, cy + a[1] * h * 0.62); q = (cx + b[0] * h * 0.62, cy + b[1] * h * 0.62)
        d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
        s = r + 0.8
        arrow(ax, (p[0] + ux * s, p[1] + uy * s), (q[0] - ux * s, q[1] - uy * s), 'varie', lw=0.9)
for cx, idx in ((24, P(0)), (64, P(0, True))):
    tile(ax, cx, 40, 11, idx, 'all'); sides(cx, 40, 11, idx)
text(ax, 24, 24, 'à l’endroit', 'encre', 's'); text(ax, 64, 24, 'retourné', 'encre', 's')
text(ax, 24, 16, 'sens inverse des aiguilles', 'varie', 's'); text(ax, 64, 16, 'sens des aiguilles', 'varie', 's')
save(fig, '44-009')
