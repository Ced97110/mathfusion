import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
from matplotlib.patches import Rectangle
text(ax, 44, 62, '1 ÷ cos x = nombre de parts', 'encre', 's')
for y, n, lab in ((44, 2, '0,5'), (26, 10, '0,1'), (8, 100, '0,01')):
    ax.add_patch(Rectangle((4, y), 66, 8, fc=FILL['sujet'], ec=COL['sujet'], lw=0.8, zorder=2))
    for i in range(1, n):
        x = 4 + 66 * i / n
        ax.plot([x, x], [y, y + 8], color=COL['sujet'], lw=0.6 if n < 100 else 0.25, zorder=3)
    text(ax, 4, y + 11.5, f'1 en parts de {lab}', 'sujet', 's', ha='left')
    text(ax, 79, y + 4, str(n), 'resultat', 'l')
save(fig, '30-080')
