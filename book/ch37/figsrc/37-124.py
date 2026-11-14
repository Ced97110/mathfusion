import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 7.0; x0 = 9; y = 14
Bx, Ax, Cx = x0, x0 + 4 * u, x0 + 10 * u
line(ax, [(Bx, y), (Cx, y)], 'sujet', lw=1.2)
for x, l in ((Bx, r'$B$'), (Ax, r'$A$'), (Cx, r'$C$')):
    disc(ax, x, y, 1.0, 'sujet'); text(ax, x, y - 4, l, 'sujet', 'm')
brace(ax, Bx, Ax, y - 6.5, 'fixe', '4', size='s'); brace(ax, Ax, Cx, y - 6.5, 'fixe', '6', size='s')
brace(ax, Bx, Cx, y + 15, 'fixe', '10', down=False, size='s')
ax.add_patch(matplotlib.patches.Arc((Ax, y), 14, 14, theta1=0, theta2=180, ec=COL['varie'], lw=1.0, zorder=3))
text(ax, Ax, y + 10.5, '180°', 'varie', 's')
text(ax, 44, 49, 'sin 180° = 0', 'varie', 'm')
text(ax, 44, 42, 'Δ = ½ × 6 × 4 × 0 = 0', 'resultat', 'm')
save(fig, '37-124')
