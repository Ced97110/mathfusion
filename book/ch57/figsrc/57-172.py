import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 17, 36, 35, 'sujet')
text(ax, 20, 46, 'type fini', 'sujet', 'm', weight='bold')
s = 5.0; ox, oy = 9, 28
P = lambda x, y: (ox + x * s, oy + y * s)
for x in range(4):
    for y in range(3):
        disc(ax, *P(x, y), 0.6, 'fixe')
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.5); arrow(ax, P(0, 0), P(0, 1), 'autre', lw=1.5)
text(ax, 20, 21, 'couples : 2 générateurs', 'sujet', 's')
for y, t in [(46, 'chapitre 58'), (22, 'chapitre 59')]:
    box(ax, 54, y - 7, 32, 14, 'resultat', label=t, size='s')
    arrow(ax, (38.5, 37), (53.5, y), 'varie', lw=1.2)
text(ax, 70, 34, 'hypothèse centrale', 'varie', 's')
text(ax, 44, 8, 'on la retrouve dans les énoncés', 'encre', 's')
save(fig, '57-172')
