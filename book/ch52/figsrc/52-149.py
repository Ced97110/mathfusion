import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ys = [78, 60, 42, 24]
box(ax, 8, 78, 72, 11, 'sujet', label=r"$b \in \ker\,\eta$ donc $\eta(b) = 0'$", size='s')
box(ax, 8, 60, 72, 11, 'varie', label=r'$\eta(ab) = \eta(a)\,\eta(b)$', size='m', weight='bold')
box(ax, 8, 42, 72, 11, 'fixe', label=r"$= \eta(a)\cdot 0' = 0'$", size='m')
box(ax, 8, 24, 72, 11, 'resultat', label=r'$ab \in \ker\,\eta$ : absorption', size='s')
for y in (78, 60, 42): arrow(ax, (44, y), (44, y - 7), 'fixe')
text(ax, 44, 17, 'et ker η est un sous-groupe de (R, +)', 'resultat', 's')
text(ax, 44, 8, 'ex. : 12 × 5 = 60, multiple de 6', 'fixe', 's')
text(ax, 84, 65, 'étape clé', 'varie', 's', ha='right') if False else None
save(fig, '52-149')
