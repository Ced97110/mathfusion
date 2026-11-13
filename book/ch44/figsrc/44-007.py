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

fig, ax = canvas(80)
box(ax, 2, 6, 84, 68, 'sujet', fill=False)
text(ax, 44, 68, 'monoïde : enchaîner', 'sujet', 'm')
box(ax, 6, 10, 36, 50, 'autre')
text(ax, 24, 54, 'groupe : + défaire', 'autre', 's')
tile(ax, 24, 36, 7, P(0)); text(ax, 24, 21, 'carreau', 'encre', 's')
text(ax, 65, 54, 'compteur', 'encre', 's')
text(ax, 65, 40, 'ajouts :\n+0, +2, +3…', 'encre', 's')
text(ax, 65, 24, 'aucun ne se défait', 'limite', 's')
save(fig, '44-007')
