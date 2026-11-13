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
xs = [14, 34, 54, 74]
for x, k in zip(xs, range(4)):
    tile(ax, x, 70, 6, P(k), 'one', 'fixe')
brace(ax, 6, 82, 60, 'varie', '4 choix pour le coin 1')
tile(ax, 26, 40, 6, P(0), 'mark')
tile(ax, 62, 40, 6, P(0, True), 'mark')
text(ax, 26, 31.5, 'endroit', 'encre', 's'); text(ax, 62, 31.5, 'retourné', 'encre', 's')
brace(ax, 18, 70, 28, 'varie', '2 choix pour la face')
text(ax, 44, 10, r'$4\times 2=8$ poses', 'resultat', 'xl')
save(fig, '44-001')
