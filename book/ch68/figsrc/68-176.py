import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
c, x0, y0 = 1.7, 8, 28
for i in range(16):
    for k in range(16):
        ax.add_patch(Rectangle((x0 + k * c, y0 + i * c), c, c, ec=COL['sujet'], fc=FILL['sujet'], lw=0.3, zorder=2))
text(ax, x0 + 8 * c, 70, '256 lignes de table', 'sujet', 's')
text(ax, x0 + 8 * c, 21, r'$2^{32-24} = 256$ classes', 'sujet', 's')
ax.add_patch(Rectangle((46, 28), 36, 36, ec=COL['fixe'], fc=FILL['fixe'], ls='--', lw=0.9, zorder=2))
text(ax, 64, 46, r'$2^{24}$', 'fixe', 'l')
text(ax, 64, 70, 'comparaisons', 'fixe', 's')
text(ax, 64, 21, 'plus de 16 millions', 'fixe', 's')
text(ax, 64, 13, 'pas à l’échelle', 'fixe', 's')
text(ax, 41, 46, 'contre', 'encre', 's')
save(fig, '68-176')
