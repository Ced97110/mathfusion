import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
x0, L = 6, 75.0; m = L / 15
box(ax, x0, 38, L, 6, 'sujet', r=0.3, label='couloir : 15 m', size='s')
sc, sa = 0.5 * m, 0.75 * m
for k in range(30):
    ax.add_patch(Rectangle((x0 + k * sc, 22), sc, 6, ec=COL['autre'], fc=FILL['autre'], lw=0.4, zorder=2))
text(ax, x0, 31.5, 'enfant : 30 pas de 0,5 m', 'autre', 's', ha='left')
for k in range(20):
    ax.add_patch(Rectangle((x0 + k * sa, 6), sa, 6, ec=COL['varie'], fc=FILL['varie'], lw=0.4, zorder=2))
text(ax, x0, 15.5, 'adulte : 20 pas de 0,75 m', 'varie', 's', ha='left')
save(fig, '11-013')
