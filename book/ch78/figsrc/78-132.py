import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 3.2
text(ax, 22, 62, '$x=(1,1,1,1)$', 'sujet', 's'); text(ax, 66, 62, '$y=(2,1,1,1)$', 'autre', 's')
text(ax, 44, 55, '$z=(-1,3,3,3)$', 'resultat', 's')
x0, y0 = 7, 26
for i in range(7):
    for j in range(4):
        ax.add_patch(Rectangle((x0 + i * u, y0 + j * u), u, u, ec=COL['sujet'], fc=FILL['sujet'], lw=0.5, zorder=2))
text(ax, x0 + 3.5 * u, y0 + 4 * u + 5, '$4\\times7=28$', 'sujet', 's')
text(ax, x0 + 3.5 * u, y0 - 3.5, '7', 'sujet', 's'); text(ax, x0 - 3, y0 + 2 * u, '4', 'sujet', 's')
text(ax, 36, 32, '=', 'encre', 'xl')
sx = 43.0
for k, side in enumerate([1, 3, 3, 3]):
    for i in range(side):
        for j in range(side):
            ax.add_patch(Rectangle((sx + i * u, y0 + j * u), u, u, ec=COL['resultat'], fc=FILL['resultat'], lw=0.5, zorder=2))
    text(ax, sx + side * u / 2, y0 - 3.5, str(side * side), 'resultat', 's')
    sx += side * u + 1.6
text(ax, 62, y0 + 4 * u + 5, '$1+9+9+9=28$', 'resultat', 's')
save(fig, '78-132')
