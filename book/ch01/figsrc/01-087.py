import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
for x0, s in [(15, '307'), (37, '991'), (59, '343')]:
    box(ax, x0, 52, 18, 10, 'sujet', label=s, size='l')
    line(ax, [(x0, 50), (x0 + 18, 50)], 'resultat', lw=2.2)
text(ax, 46, 45, 'aucun 000, aucun 1 : lecture sans piège', 'resultat', 'm')
line(ax, [(4, 40), (84, 40)], 'fixe', dash=True)
text(ax, 4, 34, 'non montré dans cet exemple :', 'encre', 'm', ha='left')
box(ax, 2, 15, 41, 14, 'fixe', fill=False, dash=True, lw=0.7)
box(ax, 45, 15, 41, 14, 'fixe', fill=False, dash=True, lw=0.7)
for x0, w, s, r in [(4, 8, '10', 'autre'), (14, 12, '000', 'limite'), (28, 12, '512', 'autre'),
                    (48, 6, '1', 'limite'), (56, 12, '000', 'autre'), (70, 12, '000', 'autre')]:
    box(ax, x0, 18, w, 8, r, label=s, size='m', dash=True)
text(ax, 20, 10, 'classe vide', 'limite', 's')
text(ax, 65, 10, 'classe égale à 1', 'limite', 's')
save(fig, '01-087')
