import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
yc = 40
box(ax, 3, 5, 82, 65, 'fixe', fill=False, dash=True)
text(ax, 44, 66, r'$G$ : 30 éléments', 'fixe', 's')
for cx, r in [(29, 'sujet'), (59, 'autre')]: disc(ax, cx, yc, 15, r, fill=False, lw=1.1)
for (dx, dy) in [(22, 0), (28, 8), (28, -8), (35, 0)]:
    disc(ax, dx, yc + dy, 1.8, 'sujet'); disc(ax, 88 - dx, yc + dy, 1.8, 'autre')
disc(ax, 44, yc, 2.2, 'resultat')
text(ax, 44, yc + 5, r'$e$', 'resultat', 'm')
text(ax, 22, 59, '5-Sylow', 'sujet', 's'); text(ax, 66, 59, 'autre 5-Sylow', 'autre', 's')
brace(ax, 15, 43, 23, 'sujet', label=r'$p-1=4$ nouveaux', down=True)
brace(ax, 45, 73, 23, 'autre', label=r'$p-1=4$ nouveaux', down=True)
text(ax, 44, 9, r'seul $e$ est commun', 'resultat', 's')
save(fig, '50-188')
