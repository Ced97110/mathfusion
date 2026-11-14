import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
P = [(6 + i * 12, 24 if i % 2 == 0 else 42) for i in range(7)]
for i in range(5):
    poly(ax, [P[i], P[i + 1], P[i + 2]], 'sujet' if i % 2 == 0 else 'autre')
line(ax, [P[1], P[2]], 'varie', lw=2.0)
text(ax, 24, 49, 'côté commun', 'varie', 's')
brace(ax, 6, 78, 21, 'fixe', label='morceau de méridien')
text(ax, 2, 17.3, 'Dunkerque', 'sujet', 's', ha='left')
text(ax, 86, 17.3, 'Barcelone', 'sujet', 's', ha='right')
save(fig, '38-007')
