import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
import math
fig, ax = canvas(84)
def reg(cx, cy, R, n, rot=90):
    return [(cx + R * math.cos(math.radians(rot + 360 * i / n)), cy + R * math.sin(math.radians(rot + 360 * i / n))) for i in range(n)]
text(ax, 44, 80, 'chaque mouvement remet le polygone', 'encre', 's')
text(ax, 44, 75, 'dans son cadre pointillé', 'fixe', 's')
for cx, n, cnt in [(15, 3, 6), (44, 4, 8), (73, 5, 10)]:
    rot = 90 if n != 4 else 45
    for cy, k in [(58, 0), (30, 1)]:
        ax.add_patch(Polygon(reg(cx, cy, 10, n, rot), closed=True, ec=COL['fixe'], fc='none', lw=1.0, ls='--', zorder=1))
        poly(ax, reg(cx, cy, 9.2, n, rot), 'sujet')
        mk = reg(cx, cy, 9.2, n, rot + 360 * k / n)[0]
        disc(ax, mk[0], mk[1], 1.6, 'varie')
    arrow(ax, (cx, 47), (cx, 41), 'varie', lw=1.4)
    text(ax, cx, 14, f'$D_{n}$', 'sujet', 'l', weight='bold')
    text(ax, cx, 7, f'{cnt} mouvements', 'encre', 's')
save(fig, '44-221')
