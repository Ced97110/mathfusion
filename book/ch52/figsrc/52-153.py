import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 20, 58, r'$R = \mathbb{Z}$', 'fixe'); text(ax, 68, 58, r"$R' = \mathbb{Z}$", 'fixe')
box(ax, 4, 6, 32, 48, 'fixe', fill=False); box(ax, 52, 6, 32, 48, 'fixe', fill=False)
ly = {0: 42, 1: 30, 2: 18}
for v, y in ly.items(): disc(ax, 20, y, 4, 'sujet' if v != 1 else 'varie', label=str(v))
disc(ax, 68, 42, 4, 'sujet', label='0'); disc(ax, 68, 18, 4, 'limite', fill=False, label='1')
for y in ly.values(): arrow(ax, (24, y), (64, 42), 'varie', lw=0.7)
text(ax, 68, 10, 'im η = {0} : sans 1', 'limite', 's')
save(fig, '52-153')
