import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 20, 68, 'bijective', 'resultat', 'm'); text(ax, 66, 68, 'pas bijective', 'limite', 'm')
for i in range(4):
    y = 55 - 14 * i
    disc(ax, 6, y, 4, 'sujet', label=str(i), size='s')
    disc(ax, 34, y, 4, 'autre', label=r'$r_%d$' % i, size='s')
    arrow(ax, (10.5, y), (29.5, y), 'resultat')
    disc(ax, 52, y, 4, 'sujet')
    disc(ax, 80, y, 4, 'autre' if i == 0 else 'fixe', fill=(i == 0), label=r'$r_%d$' % i, size='s')
    arrow(ax, (56.5, y), (75.5, 55 if i == 0 else y) if False else (75.8, 55 - 0), 'limite') if False else None
for i in range(4):
    y = 55 - 14 * i
    ax.add_patch(FancyArrowPatch((56.3, y), (75.8, 55.0 + (0 if i == 0 else 0) - 0.0), arrowstyle='-|>', mutation_scale=7, lw=1.0, color=COL['limite'], zorder=4, shrinkA=0, shrinkB=0))
text(ax, 20, 3, 'chaque rotation atteinte', 'resultat', 's'); text(ax, 66, 3, '3 rotations non atteintes', 'limite', 's')
save(fig, '45-023')
