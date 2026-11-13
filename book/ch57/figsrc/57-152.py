import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 8.0; ox, oy = 8, 12
P = lambda x, y: (ox + x * s, oy + y * s)
ker = {(0, 0), (2, 1), (4, 2)}
line(ax, [P(0, 0), P(4.6, 2.3)], 'sujet', lw=0.9, dash=True)
for x in range(5):
    for y in range(3):
        if (x, y) in ker: continue
        disc(ax, *P(x, y), 1.0, 'fixe')
for (x, y) in ker:
    disc(ax, *P(x, y), 1.5, 'sujet')
disc(ax, *P(1, 0), 1.5, 'varie')
text(ax, 20, 52, 'départ : couples', 'encre', 'm', weight='bold')
text(ax, 77, 52, 'arrivée', 'encre', 'm', weight='bold')
text(ax, 44, 39, 'noyau : envoyés sur 0', 'sujet', 's')
box(ax, 71, 28, 12, 9, 'resultat', label='0', size='l')
arrow(ax, (P(4, 2)[0] + 2, P(4, 2)[1] + 1), (70, 34), 'sujet', lw=1.0, curve=-0.25)
arrow(ax, (P(2, 1)[0] + 1.5, P(2, 1)[1] + 1), (70, 31), 'sujet', lw=1.0, curve=-0.15)
box(ax, 71, 8, 12, 9, 'fixe', label='1', size='l')
arrow(ax, (P(1, 0)[0] + 2, P(1, 0)[1]), (70, 12.5), 'varie', lw=1.0)
text(ax, P(1, 0)[0], P(1, 0)[1] - 4.5, r'$(1\,;\,0)$', 'varie', 's')
text(ax, 55, 6.5, 'pas dans le noyau', 'varie', 's')
save(fig, '57-152')
