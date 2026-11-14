import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def grid(x, y, n, c, role):
    for i in range(n):
        for j in range(n):
            ax.add_patch(Rectangle((x + i * c, y + j * c), c, c, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
text(ax, 21, 69, 'changement de base', 'fixe', 'm'); text(ax, 66, 69, 'changement de corps de base', 'sujet', 's')
line(ax, [(44, 8), (44, 66)], 'fixe', dash=True)
grid(3, 32, 4, 4.5, 'fixe'); grid(24, 32, 4, 4.5, 'fixe')
text(ax, 12, 27, r'$\mathbb{Q}$', 'fixe', 's'); text(ax, 33, 27, r'$\mathbb{Q}$', 'fixe', 's')
text(ax, 22, 14, 'même taille', 'fixe', 's')
grid(50, 32, 4, 4.5, 'sujet'); grid(74, 38, 2, 4.5, 'autre')
text(ax, 59, 27, r'$\mathbb{Q}$', 'sujet', 's'); text(ax, 79, 33, r'$\mathbb{Q}(\sqrt{2})$', 'autre', 's')
text(ax, 59, 54, r'$4\times4$', 'sujet', 's'); text(ax, 79, 54, r'$2\times2$', 'autre', 's')
text(ax, 66, 14, 'tailles différentes', 'sujet', 's')
save(fig, '77-010')
