import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 63, r'$T=\{1\}$ : 1 garde son chapeau', 'sujet', 's')
text(ax, 64, 48, 'chapeau reçu par 1, 2, 3', 'fixe', 's')
for r, (digs, lab) in enumerate([('123', 'chacun a le sien'), ('132', '2 et 3 échangent')]):
    y = 28 - r * 16
    text(ax, 2, y + 5, lab, 'fixe', 's', ha='left')
    for i, d in enumerate(digs): box(ax, 47 + i * 13, y, 12, 10, 'fixe' if i == 0 else 'varie', label=d, size='l')
text(ax, 44, 4, r'$(3-1)!=2$ façons', 'resultat', 'm')
save(fig, '80-372')
