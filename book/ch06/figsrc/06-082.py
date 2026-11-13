import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(x, y, wd, ht, role, lw=0.5):
    ax.add_patch(Rectangle((x, y), wd, ht, ec=COL[role], fc=FILL[role], lw=lw, zorder=2))
fig, ax = canvas(60)
x0, wd = 8, 72
for i in range(4):
    cell(x0 + i * wd / 4, 40, wd / 4, 8, 'sujet' if i < 3 else 'fixe')
for i in range(100):
    cell(x0 + i * wd / 100, 14, wd / 100, 8, 'autre' if i < 75 else 'fixe', lw=0.15)
xm = x0 + wd * 3 / 4
line(ax, [(xm, 49), (xm, 13)], 'resultat', dash=True)
text(ax, 38, 31, 'même part', 'resultat', 's')
text(ax, 44, 54, 'rapport : 3 élèves sur 4', 'sujet', 's')
text(ax, 44, 7, '75 sur 100 = 75 %', 'autre', 's')
save(fig, '06-082')
