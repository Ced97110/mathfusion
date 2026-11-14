import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
s = 2.6; gap = 8
cases = [(2, 6, 16, 'limite'), (4, 8, 24, 'limite'), (3, 7, 20, 'resultat')]
tot = sum((l + 4) * s for l, _, _, _ in cases) + 2 * gap
x = (W - tot) / 2; yb = 26
text(ax, 44, 57, 'longueur = largeur + 4', 'varie', 'm')
for l, L, p, r in cases:
    ax.add_patch(Rectangle((x, yb), l * s, l * s, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((x + l * s, yb), 4 * s, l * s, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
    text(ax, x + l * s + 2 * s, yb + l * s / 2, '+4', 'varie', 's')
    cx = x + (l + 4) * s / 2
    text(ax, cx, yb - 4, f'{l} et {L}', 'encre', 's')
    text(ax, cx, yb - 11, f'tour {p} m', r, 'm', weight='bold')
    x += (l + 4) * s + gap
text(ax, 44, 7, 'on cherche la largeur : tour 20', 'resultat', 's')
save(fig, '16-004')
