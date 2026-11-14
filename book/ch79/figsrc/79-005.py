import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
disc(ax, 22, 32, 6, 'sujet', label='12', size='l'); disc(ax, 66, 32, 6, 'autre', label='20', size='l')
disc(ax, 44, 54, 6, 'resultat', label='60', size='l'); disc(ax, 44, 10, 6, 'resultat', label='4', size='l')
for (p, q) in [((25, 37), (41, 49)), ((63, 37), (47, 49)), ((41, 15), (25, 27)), ((47, 15), (63, 27))]:
    line(ax, [p, q], 'resultat', lw=1.6)
text(ax, 58, 54, 'PPCM', 'resultat', 'm', ha='left'); text(ax, 58, 10, 'PGCD', 'resultat', 'm', ha='left')
text(ax, 44, 32, 'pas de lien', 'limite', 's')
line(ax, [(30, 32), (37, 32)], 'limite', dash=True); line(ax, [(51, 32), (58, 32)], 'limite', dash=True)
save(fig, '79-005')
