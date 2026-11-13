import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'deux bases du plan', 'fixe', 's')
xs = [14, 50]
for x, l in zip(xs, ['(1, 0)', '(0, 1)']):
    box(ax, x, 46, 24, 9, 'sujet', label=l, size='s')
for x, l in zip(xs, ['(3, 1)', '(1, 2)']):
    box(ax, x, 14, 24, 9, 'autre', label=l, size='s')
for x in xs:
    arrow(ax, (x + 12, 45), (x + 12, 24), 'resultat', both=True)
text(ax, 2, 50.5, 'base', 'sujet', 's', ha='left')
text(ax, 2, 18.5, 'base', 'autre', 's', ha='left')
text(ax, 44, 34, 'un pour un', 'resultat', 's', weight='bold')
text(ax, 44, 4, '2 vecteurs et 2 vecteurs', 'resultat', 'm')
save(fig, '58-179')
