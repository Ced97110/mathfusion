import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
s = 4.4
def grid(x0, y0, n, cols, role):
    for k in range(n):
        ax.add_patch(Rectangle((x0 + (k % cols) * s, y0 - (k // cols) * s), s - 0.4, s - 0.4, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
grid(4, 30, 1, 1, 'sujet'); grid(26, 30, 2, 2, 'varie'); grid(52, 30, 10, 5, 'resultat')
text(ax, 6, 22, r'$e_{12}$', 'sujet', 's'); text(ax, 31, 22, r'$2e_{12}$', 'varie', 's'); text(ax, 62, 22, r'$10e_{12}$', 'resultat', 's')
arrow(ax, (11, 32), (24, 32), 'encre'); text(ax, 17.5, 37, r'$\times2\ (L_2)$', 'encre', 's')
arrow(ax, (37, 32), (50, 32), 'encre'); text(ax, 43.5, 37, r'$\times5\ (L_1)$', 'encre', 's')
arrow(ax, (6, 15), (72, 15), 'resultat', curve=0.0)
text(ax, 44, 10, r'$L_1L_2$ en une fois : $\times10$', 'resultat', 's')
save(fig, '76-074')
