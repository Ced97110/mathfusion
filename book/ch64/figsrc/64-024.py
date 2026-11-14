import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'deux groupes non abéliens', 'fixe', 'm', weight='bold')
cards = [(2, 'sujet', r'$S_4$ : 24 éléments', 'resultat', 'se découpe', '24, 12, 4, 1'),
         (46, 'autre', r'$A_5$ : 60 éléments', 'limite', 'ne se découpe pas', 'aucun étage abélien')]
for x, role, title, rr, res, sub in cards:
    box(ax, x, 4, 40, 50, 'fixe', fill=False)
    text(ax, x + 20, 47, title, role, 's', weight='bold')
    text(ax, x + 20, 40, 'non abélien', 'fixe', 's')
    arrow(ax, (x + 20, 36), (x + 20, 29), rr)
    box(ax, x + 3, 18, 34, 10, rr, label=res, size='s')
    text(ax, x + 20, 11, sub, rr, 's')
save(fig, '64-024')
