import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# famille indépendante (2 vecteurs) comparée à famille génératrice (3 vecteurs)
text(ax, 44, 59, 'dans le plan', 'encre', 'm')
text(ax, 4, 49, 'famille indépendante', 'sujet', 's', ha='left')
for i, v in enumerate(['(1, 0)', '(1, 1)']):
    box(ax, 4 + i * 20, 36, 18, 9, 'sujet', label=v, size='s', r=0.5)
text(ax, 4, 28, 'famille génératrice', 'autre', 's', ha='left')
for i, v in enumerate(['(1, 0)', '(0, 1)', '(1, 1)']):
    box(ax, 4 + i * 20, 15, 18, 9, 'autre', label=v, size='s', r=0.5)
text(ax, 77, 40.5, '2', 'sujet', 'l', weight='bold')
text(ax, 77, 19.5, '3', 'autre', 'l', weight='bold')
text(ax, 77, 30, '≤', 'resultat', 'xl', weight='bold')
box(ax, 20, 2, 48, 8, 'resultat', label='indépendante ≤ génératrice', size='s', r=0.5)
save(fig, '58-194')
