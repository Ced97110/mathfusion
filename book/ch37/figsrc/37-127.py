import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 7.0; x0 = 9; y = 46
Bx, Ax, Cx = x0, x0 + 4 * u, x0 + 10 * u
line(ax, [(Bx, y), (Cx, y)], 'sujet', lw=1.2)
for x, l in ((Bx, '$B$'), (Ax, '$A$'), (Cx, '$C$')):
    disc(ax, x, y, 1.0, 'sujet'); text(ax, x, y - 4, l, 'sujet', 'm')
ax.add_patch(matplotlib.patches.Arc((Ax, y), 14, 14, theta1=0, theta2=180, ec=COL['varie'], lw=1.0, zorder=3))
text(ax, Ax, y + 10.5, '180°', 'varie', 's')
box(ax, 22, 28, 44, 8, 'varie', label='sin 180° = 0', size='m')
arrow(ax, (44, 27), (44, 22), 'limite')
box(ax, 22, 14, 44, 8, 'limite', label='2R = 10 ÷ 0', size='m')
arrow(ax, (44, 13), (44, 8), 'limite')
box(ax, 22, 0.5, 44, 8, 'limite', label='R n’existe pas', size='m')
save(fig, '37-127')
