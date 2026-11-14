import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 10; x0 = 10; y0 = 10
for i in range(3):
    for j in range(3):
        d = i == j
        ax.add_patch(Rectangle((x0 + j * c, y0 + (2 - i) * c), c, c, ec=COL['fixe'], fc=FILL['resultat'] if d else 'white', lw=0.7, zorder=2))
        text(ax, x0 + j * c + c / 2, y0 + (2 - i) * c + c / 2, '1' if d else '0', 'resultat' if d else 'fixe', 'm')
text(ax, 4, y0 + 15, r'$r$', 'encre', 'm'); text(ax, x0 + 15, y0 + 34, r'$s$', 'encre', 'm')
ax.add_patch(Rectangle((x0 + c, y0 + c), c, c, ec=COL['varie'], fc='none', lw=2, zorder=3))
ax.add_patch(Rectangle((x0 + 2 * c, y0 + c), c, c, ec=COL['autre'], fc='none', lw=2, zorder=3))
text(ax, 62, 33, r'$\delta_{22} = 1$ : $r = s$', 'varie', 's')
text(ax, 62, 20, r'$\delta_{23} = 0$ : $r \neq s$', 'autre', 's')
save(fig, '73-141')
