import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(52)
brace(ax, 20, 80, 42, 'fixe', 'même barre : 60 cm', down=False)
for i, (b, s) in enumerate([(3, '20 cm'), (4, '15 cm'), (6, '10 cm')]):
    y = 28 - i * 13
    bar(ax, 20, y, 60, 8, ['varie'] + ['sujet'] * (b - 1))
    text(ax, 10, y + 4, f'$b={b}$', 'sujet', 'l')
    text(ax, 20 + 30 / b, y + 4, s, 'varie', 's')
save(fig, '06-025')
