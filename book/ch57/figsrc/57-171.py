import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 22, 78, 'type fini : couples', 'sujet', 's', weight='bold')
s = 6.0; ox, oy = 8, 36
P = lambda x, y: (ox + x * s, oy + y * s)
for x in range(5):
    for y in range(4):
        if (x, y) not in [(4, 1), (4, 0), (0, 1)]: disc(ax, *P(x, y), 0.7, 'fixe')
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.6)
arrow(ax, P(0, 0), P(0, 1), 'autre', lw=1.6)
text(ax, P(1, 0)[0] + 1, P(1, 0)[1] + 2.5, r'$(1\,;\,0)$', 'sujet', 's', ha='left')
text(ax, P(0, 1)[0] + 3, P(0, 1)[1] + 3.5, r'$(0\,;\,1)$', 'autre', 's')
arrow(ax, P(0, 0), P(3, 0), 'sujet', lw=0.9); arrow(ax, P(3, 0), P(3, 2), 'autre', lw=0.9)
disc(ax, *P(3, 2), 1.5, 'resultat')
text(ax, P(1.5, 0)[0], P(1.5, 0)[1] - 3.5, r'$m\times(1\,;\,0)$', 'sujet', 's')
text(ax, P(3, 2)[0] + 2, P(3, 2)[1] + 3.5, r'$(m\,;\,n)$', 'resultat', 's')
text(ax, P(3, 1)[0] + 2, P(3, 1)[1] + 0.5, r'$n\times(0\,;\,1)$', 'autre', 's', ha='left')
text(ax, 66, 78, 'pas de type fini', 'limite', 's', weight='bold')
text(ax, 66, 72, 'polynômes sur les entiers', 'limite', 's')
for k in range(6):
    gen = k < 3
    box(ax, 48, 10 + k * 8, 20, 6.5, 'sujet' if gen else 'limite', dash=not gen)
line(ax, [(47, 10 + 3 * 8 - 0.7), (70, 10 + 3 * 8 - 0.7)], 'varie', lw=1.0, dash=True)
text(ax, 58, 5, 'degré croissant ↑', 'encre', 's')
text(ax, 58, 10 + 6 * 8 + 1.5, '…', 'limite', 'm')
text(ax, 24, 24, 'degré maximal', 'varie', 's')
arrow(ax, (38, 26), (46, 33), 'varie', lw=0.9)
text(ax, 71, 22, 'engendrés', 'sujet', 's', ha='left', weight='bold')
text(ax, 71, 46, 'manquent', 'limite', 's', ha='left', weight='bold')
save(fig, '57-171')
