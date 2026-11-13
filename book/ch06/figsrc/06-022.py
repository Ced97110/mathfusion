import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(58)
for y, b, name, frac in [(40, 4, 'des quarts', '1/4'), (24, 5, 'des cinquièmes', '1/5'), (8, 100, 'des centièmes', '1/100')]:
    text(ax, 6, y + 12, f'$b={b}$ : {name}', 'sujet', 'm', ha='left')
    text(ax, 82, y + 12, f'une part : ${frac}$', 'varie', 's', ha='right')
    if b < 100:
        bar(ax, 6, y, 76, 8, ['varie'] + ['sujet'] * (b - 1))
    else:
        box(ax, 6, y, 76, 8, 'sujet', r=0.1)
        ax.add_patch(Rectangle((6, y), 0.76, 8, ec='none', fc=COL['varie'], zorder=3))
save(fig, '06-022')
