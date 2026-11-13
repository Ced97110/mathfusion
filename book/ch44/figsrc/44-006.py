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

fig, ax = canvas(88)
box(ax, 2, 44, 84, 40, 'sujet')
text(ax, 44, 79, 'groupe : les 8 mouvements', 'sujet', 'm')
poses = [P(k) for k in range(4)] + [P(k, True) for k in range(4)]
for i, p in enumerate(poses):
    tile(ax, 9 + 10 * i, 62, 4, p)
text(ax, 44, 38, 'deux propriétés', 'encre', 's')
tile(ax, 7, 20, 4, P(1)); tile(ax, 19, 20, 4, P(0, True))
arrow(ax, (25, 20), (30, 20), 'varie'); tile(ax, 37, 20, 4, [3 - ((i + 1) % 4) for i in range(4)], role='resultat')
text(ax, 22, 8, 'enchaîner : 2 → 1', 'encre', 's')
tile(ax, 52, 20, 4, P(1)); arrow(ax, (58, 20), (70, 20), 'varie', both=True); tile(ax, 76, 20, 4, P(3))
text(ax, 64, 8, 'défaire : le retour', 'encre', 's')
save(fig, '44-006')
