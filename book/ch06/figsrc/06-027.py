import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(52)
text(ax, 44, 47, 'couper la tablette en', 'encre', 'm')
box(ax, 6, 26, 24, 14, 'sujet'); box(ax, 32, 26, 24, 14, 'sujet'); line(ax, [(44, 27), (44, 39)], 'varie')
box(ax, 58, 26, 24, 14, 'limite', fill=False, dash=True)
line(ax, [(60, 28), (80, 38)], 'limite'); line(ax, [(60, 38), (80, 28)], 'limite')
for x, a, b, r in [(18, '1 part', '0 trait', 'varie'), (44, '2 parts', '1 trait', 'varie'), (70, '0 part', 'impossible', 'limite')]:
    text(ax, x, 20, a, 'encre', 'm'); text(ax, x, 11, b, r, 'm')
save(fig, '06-027')
