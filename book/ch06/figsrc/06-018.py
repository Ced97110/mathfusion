import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(58)
text(ax, 44, 53, '« 12 sur 30 »', 'encre', 'l')
for k in range(30):
    r, c = divmod(k, 6)
    disc(ax, 9 + c * 6, 42 - r * 6, 2.3, 'sujet' if k < 12 else 'fixe')
text(ax, 66, 39, '12', 'sujet', 'xl')
line(ax, [(59, 31), (73, 31)], 'encre')
text(ax, 66, 23, '30', 'fixe', 'xl')
text(ax, 80, 39, 'partie', 'sujet', 's')
text(ax, 80, 23, 'tout', 'fixe', 's')
text(ax, 24, 6, '12 jouent, sur 30 élèves', 'encre', 's')
save(fig, '06-018')
