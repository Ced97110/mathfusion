import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, w_ = 6.5, 75
for i in range(15):
    ax.add_patch(Rectangle((x0 + i * w_ / 15, 30), w_ / 15, 8, ec=COL['sujet'], fc=FILL['sujet'] if i < 7 else FILL['encre'], lw=0.6, zorder=2))
text(ax, 6, 54, '7/15', 'sujet', 'l', ha='left')
brace(ax, x0, x0 + 35, 38, 'sujet', label='7 prises', down=False)
line(ax, [(x0 + 37.5, 30), (x0 + 37.5, 47)], 'fixe', dash=True)
text(ax, x0 + 39.5, 47.5, 'moitié : 7,5 parts', 'fixe', 's', ha='left')
brace(ax, x0, x0 + w_, 30, 'fixe', label='15 parts de l’unité', down=True)
arrow(ax, (44, 22.5), (44, 15.5), 'varie')
box(ax, 14, 5, 60, 10, 'resultat', label='7/15 est proche de 1/2')
save(fig, '10-069')
