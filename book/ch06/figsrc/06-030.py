import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(44)
f = numberline(ax, 8, 72, 14, 0, 2, step=1)
disc(ax, f(3 / 8), 14, 1.8, 'sujet'); text(ax, f(3 / 8), 20, '3/8', 'sujet', 's')
disc(ax, f(1), 14, 1.8, 'fixe', fill=False); text(ax, f(1), 20, '8/8', 'fixe', 's')
disc(ax, f(11 / 8), 14, 1.8, 'fixe'); text(ax, f(11 / 8), 20, '11/8', 'fixe', 's')
brace(ax, f(0), f(1), 25, 'sujet', '$a<b$ : entre 0 et 1', down=False)
save(fig, '06-030')
