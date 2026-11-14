import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 4, 68, r'une erreur : $\approx$ 0,066', 'sujet', 'm', ha='left')
for k in range(30):
    disc(ax, 8 + 6 * (k % 10), 60 - 6 * (k // 10), 2.3, 'sujet')
text(ax, 4, 34, r'deux erreurs ou plus : $\approx$ 0,002', 'autre', 'm', ha='left')
disc(ax, 8, 27, 2.3, 'autre')
text(ax, 14, 27, r'une pastille $\approx$ 0,002', 'fixe', 's', ha='left')
text(ax, 44, 12, '30 pastilles contre 1', 'resultat', 'l')
save(fig, '68-097')
