import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 10.0; ox, oy = 18.0, 16.0
P = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [P(-0.5, -0.25), P(6.5, 3.25)], 'sujet', lw=1.3)
line(ax, [P(0.5, -0.25), P(6.5, 2.75)], 'autre', lw=1.3)
line(ax, [P(-0.5, 0.0), P(6.5, 3.5)], 'limite', lw=1.0, dash=True)
A = {(0, 0), (2, 1), (4, 2), (6, 3)}; B = {(1, 0), (3, 1), (5, 2)}
for i in range(0, 7):
    for j in range(0, 4):
        if (i, j) in A: disc(ax, *P(i, j), 1.0, 'sujet')
        elif (i, j) in B: disc(ax, *P(i, j), 1.0, 'autre')
        else: disc(ax, *P(i, j), 0.5, 'fixe')
disc(ax, *P(0, 0.25), 0.7, 'limite', fill=False)
line(ax, [P(0, 0), P(2, 0), P(2, 1)], 'varie', lw=1.5)
line(ax, [P(3, 1), P(5, 1), P(5, 2)], 'varie', lw=1.5)
text(ax, P(1, 0)[0], P(1, 0)[1] - 4.3, 'avance 2', 'varie', 's')
text(ax, P(2, 0.5)[0] + 7, P(2, 0.5)[1] - 1, 'monte 1', 'varie', 's')
text(ax, 44, 68, 'deux classes : même pente', 'encre', 'm')
text(ax, 62, 61, r'classe de $(0\,;\,0)$', 'sujet', 's')
text(ax, 70, 13, r'classe de $(1\,;\,0)$', 'autre', 's')
text(ax, 2, 5, r'tirets : $(0\,;\,\frac{1}{4})$, aucun point entier', 'limite', 's', ha='left')
save(fig, '57-147')
