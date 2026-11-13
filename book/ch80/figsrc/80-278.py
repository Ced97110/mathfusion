import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
hy = 54; P = (44, hy)
line(ax, [(2, hy), (86, hy)], 'fixe', lw=0.8)
text(ax, 84, hy + 3, r'$h$', 'fixe', 'm')
for xb in (12, 76):
    line(ax, [(xb, 6), P], 'sujet', lw=1.3)
for y in (9, 16, 24, 33, 42, 49):
    t = (hy - y) / (hy - 6); xl = 44 + (12 - 44) * t; xr = 44 + (76 - 44) * t
    line(ax, [(xl, y), (xr, y)], 'varie', lw=1.1)
disc(ax, P[0], P[1], 1.6, 'limite')
text(ax, 44, hy + 5, r'$P_\infty$', 'limite', 'm')
text(ax, 10, 17, r'$D_1$', 'sujet', 'm'); text(ax, 78, 17, r'$D_2$', 'sujet', 'm')
text(ax, 44, 3.5, 'traverse longue', 'varie', 's')
text(ax, 56, 42, 'courte', 'varie', 's', ha='left')
save(fig, '80-278')
