import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(66)
text(ax, 44, 61, '1 m coupé en $b$ parts égales', 'encre', 'm')
for i, (b, s) in enumerate([(4, '25 cm'), (5, '20 cm'), (10, '10 cm')]):
    y = 42 - i * 14
    bar(ax, 22, y, 48, 8, ['varie'] + ['sujet'] * (b - 1))
    text(ax, 11, y + 4, f'$b={b}$', 'sujet', 'l')
    text(ax, 79, y + 4, s, 'varie', 'm')
text(ax, 44, 6, 'une part = $1/b$ de l’unité', 'varie', 's')
save(fig, '06-017')
