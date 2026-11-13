import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import FancyArrowPatch
fig, ax = canvas(70)
text(ax, 22, 66, 'Sans axiomes', 'limite', 'm')
text(ax, 66, 66, "Avec une liste d'axiomes", 'sujet', 'm')
for x in (7, 51):
    box(ax, x, 52, 30, 7, 'resultat', label='3 + 2 = 5')
# colonne gauche
for y, lab in ((40, 'règle 1'), (28, 'règle 2'), (16, 'règle 3')):
    box(ax, 7, y, 30, 7, 'fixe', label=lab)
for y in (52, 40, 28):
    arrow(ax, (22, y), (22, y - 5), 'varie')
text(ax, 24, 49.5, 'pourquoi ?', 'varie', 's', ha='left')
text(ax, 22, 11, '…', 'limite', 'l')
ax.add_patch(FancyArrowPatch((22, 9), (22, 2), arrowstyle='-|>', mutation_scale=7, lw=1.0,
             color=COL['limite'], ls='--', zorder=4, shrinkA=0, shrinkB=0))
# colonne droite
for y, lab in ((40, 'règle 1'), (28, 'règle 2')):
    box(ax, 51, y, 30, 7, 'resultat', label=lab)
for a, b in ((22, 28), (35, 40), (47, 52)):
    arrow(ax, (66, a), (66, b), 'resultat')
text(ax, 68, 37.5, 'on démontre', 'resultat', 's', ha='left')
box(ax, 48, 12, 36, 10, 'sujet', lw=1.4, label='axiomes : admis sans preuve', size='s')
line(ax, [(48, 9), (84, 9)], 'sujet', lw=1.6)
text(ax, 66, 5, "on s'arrête ici", 'sujet', 's')
save(fig, '01-025')
