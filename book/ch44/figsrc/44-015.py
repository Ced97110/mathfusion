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

fig, ax = canvas(92)
text(ax, 44, 88, '4 rotations : 4 poses', 'encre', 's')
for i, x in enumerate([14, 34, 54, 74]): tile(ax, x, 74, 6, P(i), role='fixe')
text(ax, 44, 57, 'aucune ne donne la pose voulue', 'limite', 's')
tile(ax, 18, 36, 6, P(0)); line(ax, [(3, 36), (33, 36)], 'fixe', dash=True)
text(ax, 7, 40.5, 'axe', 'fixe', 's'); text(ax, 18, 26, 'départ', 'encre', 's')
arrow(ax, (35, 36), (58, 36), 'varie'); text(ax, 46.5, 41, 'réflexion', 'varie', 's')
tile(ax, 70, 36, 6, P(0, True), role='resultat'); text(ax, 70, 26, 'pose voulue', 'resultat', 's')
save(fig, '44-015')
