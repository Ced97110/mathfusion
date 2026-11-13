import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 22, 53, 'métrique', 'sujet', 'm', weight='bold'); text(ax, 66, 53, 'États-Unis', 'autre', 'm', weight='bold')
line(ax, [(44, 4), (44, 56)], 'fixe', dash=True)
text(ax, 22, 42, '1 km = 1 000 m', 'sujet', 's')
for i, d in enumerate('1000'):
    box(ax, 6 + i * 8, 26, 8, 9, 'sujet' if i == 0 else 'fixe', label=d, size='l')
text(ax, 22, 19, 'un 1 suivi de zéros', 'resultat', 's')
for k, t in enumerate(['1 mile = 5 280 pieds', '1 yard = 3 pieds', '1 pied = 12 po']):
    box(ax, 47, 36 - k * 10, 39, 8, 'autre', label=t, size='s')
text(ax, 66, 10, 'aucune règle commune', 'limite', 's')
save(fig, '11-022')
