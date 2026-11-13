import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
y = 22
f = numberline(ax, 8, 66, y, 3.5, 5.5, step=0.5, arrow_right=False, every=1)
ax.add_patch(Rectangle((f(4), y + 0.6), f(5) - f(4), 2.0, fc=FILL['sujet'], ec=COL['sujet'], lw=0.6, zorder=2))
ax.add_patch(Rectangle((f(5), y + 0.6), f(5.5) - f(5), 2.0, fc=FILL['limite'], ec=COL['limite'], lw=0.6, zorder=2))
text(ax, f(4.5) - 3, y + 7, 'entre 4° et 5°', 'sujet', 's')
text(ax, f(5.5) + 1, y + 7, 'plus de 5°', 'limite', 's', ha='left')
line(ax, [(f(5), y - 1.5), (f(5), y + 4)], 'fixe', dash=True)
disc(ax, f(4.76), y, 1.5, 'resultat')
arrow(ax, (f(4.76), y + 16), (f(4.76), y + 2), 'resultat')
box(ax, f(4.76) - 14, y + 17, 28, 9, 'resultat', label='angle ≈ 4,76°')
text(ax, f(4.76), y - 10, '4,76° < 5° : permis', 'resultat', 's')
save(fig, '33-009')
