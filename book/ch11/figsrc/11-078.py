import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 12, 38, r'$L$', 'sujet', 'xl'); text(ax, 12, 29, 'longueur', 'sujet', 's')
x0, y0, w, h = 30, 8, 44, 30
ax.add_patch(Rectangle((x0, y0), w, h, fc=FILL['fixe'], ec=COL['fixe'], lw=1.0, zorder=2))
line(ax, [(x0, y0 + h), (x0 + w, y0 + h)], 'sujet', lw=2.6)
arrow(ax, (20, 38), (x0 - 1.5, y0 + h), 'varie')
text(ax, x0 + w / 2, y0 + h + 4.5, r'$L$ = 12 m', 'sujet', 'm')
text(ax, x0 + w / 2, y0 + h / 2, 'rectangle', 'fixe', 's'); text(ax, x0 + w + 2, y0 + h / 2, '8 m', 'fixe', 's', ha='left')
save(fig, '11-078')
