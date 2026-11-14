import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ds = [1, 2, 3, 4, 6, 12]
for i, d in enumerate(ds):
    box(ax, 3 + 13.5 * i, 44, 11, 9, 'sujet' if i == 0 else 'fixe', label=str(d))
text(ax, 8.5, 57, 'minimal', 'sujet', 's')
arrow(ax, (8.5, 44), (8.5, 33), 'varie')
for i, d in enumerate(ds):
    role = 'resultat' if i == 0 else ('varie' if d in (2, 3) else 'fixe')
    box(ax, 3 + 13.5 * i, 22, 11, 9, role, label=str(d))
text(ax, 8.5, 17, 'placé', 'resultat', 's')
text(ax, 30, 17, 'rien dessous', 'varie', 's')
text(ax, 44, 6, 'puis on recommence', 'encre', 's')
save(fig, '80-267')
